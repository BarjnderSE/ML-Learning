import streamlit as st

# Page Title
st.title("Steps of Machine Learning")

# Introduction
st.write("""
Machine Learning involves a series of steps to turn raw data into actionable insights. 
Here are the 11 key steps in the ML process, explained simply with examples.
""")

# Step 1: Define the Problem
st.subheader("1. Define the Problem")
st.write("""
Before you start, clearly define what you are trying to achieve.
- **Example**: Predict house prices based on size, location, and other features.
""")

# Step 2: Data Preprocessing
st.subheader("2. Data Preprocessing")
st.write("""
Clean and prepare the raw data for analysis. This includes handling missing values, removing duplicates, and normalizing data.
- **Example**: If a dataset has empty values for some rows, fill them with an average or drop those rows.
""")

# Step 3: Choose a Model Based on Data
st.subheader("3. Choose a Model Based on Data")
st.write("""
Select the appropriate algorithm depending on your data and problem type.
- **Example**: Use Linear Regression for predicting continuous values or K-Means for clustering.
""")

# Step 4: Split the Data
st.subheader("4. Split the Data")
st.write("""
Divide the dataset into training and testing sets. The training set is used to train the model, while the testing set evaluates it.
- **Example**: 80% of data for training and 20% for testing.
""")

# Step 5: Train the Model
st.subheader("5. Train the Model")
st.write("""
Use the training data to teach the model how to make predictions or classifications.
- **Example**: Train a Decision Tree on customer purchase history.
""")

# Step 6: Evaluate the Model
st.subheader("6. Evaluate the Model")
st.write("""
Test the model using the testing data and check its performance using metrics like accuracy, precision, and recall.
- **Example**: An accuracy of 85% means the model predicts correctly 85% of the time.
""")

# Step 7: Hyperparameter Tuning
st.subheader("7. Hyperparameter Tuning")
st.write("""
Adjust the parameters of the model to improve its performance.
- **Example**: Changing the learning rate in a Neural Network to achieve better results.
""")

# Step 8: Train and Test the Model
st.subheader("8. Train and Test the Model")
st.write("""
Iteratively train and test the model to ensure it generalizes well to unseen data.
- **Example**: Train with 70% of data, validate with 20%, and test with 10%.
""")

# Step 9: Finalize the Model
st.subheader("9. Finalize the Model")
st.write("""
Choose the best model based on evaluation metrics and prepare it for deployment.
- **Example**: Save the best-performing model for use in production.
""")

# Step 10: Deploy the Model
st.subheader("10. Deploy the Model")
st.write("""
Deploy the model in a real-world environment so users can interact with it.
- **Example**: A recommendation system on an e-commerce website.
""")

# Step 11: Retest and Update the Model
st.subheader("11. Retest and Update the Model")
st.write("""
Monitor the model’s performance in production and update it as new data comes in.
- **Example**: Retrain a spam detection model to recognize new types of spam emails.
""")

# Closing Note
st.write("These steps ensure a structured approach to building and deploying reliable Machine Learning models.")
