# Credit Card Score Classifier
This project aims to classify credit card applications using a random forest classifier. The classifier predicts whether an applicant is likely to be approved or rejected based on various features.

# Dataset
The dataset used for training and testing the classifier : https://statso.io/credit-score-classification-case-study/

# Requirements
Make sure you have the following dependencies installed:
* Python 3.7 or above
* scikit-learn
* pandas
* streamlit

# Model Training
The random forest classifier is trained using scikit-learn's RandomForestClassifier class. The training code is not included in this repository, as it depends on the specific dataset used.

If you want to train the classifier with your own dataset, you can write a script that performs the following steps:
Load the dataset into a pandas DataFrame.
Preprocess the data (e.g., handle missing values, encode categorical variables).
Split the data into training and testing sets.
Initialize an instance of the RandomForestClassifier class.
Fit the classifier to the training data.
Evaluate the classifier's performance on the testing data.
You can then save the trained classifier using scikit-learn's model persistence methods, such as joblib.dump().

# About
This project is developed using Python and the scikit-learn library. The user interface is created using Streamlit, a Python library for building interactive web applications. The classifier is trained using a random forest algorithm, which is known for its effectiveness in handling tabular data classification tasks.

Feel free to explore the code and modify it according to your needs. If you have any questions or suggestions, please open an issue in this repository.

Happy classifying!







