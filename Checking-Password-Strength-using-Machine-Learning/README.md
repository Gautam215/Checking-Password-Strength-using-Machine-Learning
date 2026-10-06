# Checking-Password-Strength-using-Machine-Learning
 
This project predicts password strength from character-level features using the supplied dataset and a Logistic Regression classifier. The Streamlit app reuses its cached model across interactions.

# Dataset

The dataset used for training the model is stored in the "Password Strength.csv" file and contains a list of passwords along with their corresponding strength category. The dataset is preprocessed by dropping the rows with missing values and visualizing the distribution of the password strength categories. Let the features be

Password - 670k unique values for password collected online

Strength - three values(0 , 1 , 2) i.e. 0 for weak, 1 for medium, 2 for strong.

Strength of the password based on rules(such as containing digits, special symbols , etc.)

# Feature Engineering
To convert the password strings into machine-readable features, we use the TF-IDF vectorizer at the character level. This converts each password into a vector of numerical features that capture the importance of each character in the password.

# Model Training and Evaluation
The notebook splits the dataset into training and testing sets and evaluates Logistic Regression. The Streamlit app trains that sparse-compatible classifier on the available dataset once, then caches it for subsequent interactions.

# Usage
To use the password strength prediction model, simply run the Python code and input a password when prompted. The model will preprocess the password using the same vectorizer used for training the model and predict its strength category.

# Dependencies
The code requires the following Python libraries to be installed:

Pandas

numpy

Seaborn

Sklearn
# Acknowledgements
This project was inspired by the Kaggle dataset on password strength and the corresponding competition. We also acknowledge the open-source Python libraries used in this project and their contributors.
