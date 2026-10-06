import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "checking_password_strength.py"


class PasswordStrengthAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = AppTest.from_file(str(APP_PATH), default_timeout=300).run()

    def test_custom_password_is_hidden_and_classified(self):
        password = "Mix!Caps42-ü"
        field = self.app.text_input[0]

        self.assertEqual(field.proto.type, 1)
        field.set_value(password).run()
        self.assertFalse(self.app.exception)

        self.app.button[0].click().run()

        messages = [element.value for elements in (
            self.app.error,
            self.app.warning,
            self.app.success,
        ) for element in elements]
        self.assertTrue(
            any(message in {"Weak Password", "Medium Password", "Strong Password"}
                for message in messages)
        )
        self.assertNotIn(password, str(self.app.text))

    def test_weak_medium_and_strong_predictions(self):
        cases = {
            "qwerty": "Weak Password",
            "password": "Medium Password",
            "AVYq1lDE4MgAZfNt": "Strong Password",
        }
        for password, expected in cases.items():
            self.app.text_input[0].set_value(password).run()
            self.app.button[0].click().run()
            messages = [element.value for elements in (
                self.app.error,
                self.app.warning,
                self.app.success,
            ) for element in elements]
            self.assertIn(expected, messages)

    def test_empty_password_shows_prompt(self):
        self.app.text_input[0].set_value("").run()
        self.app.button[0].click().run()
        self.assertEqual(self.app.info[0].value, "Please enter a password.")


if __name__ == "__main__":
    unittest.main()
