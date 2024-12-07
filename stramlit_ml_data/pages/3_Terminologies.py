import streamlit as st

# Title for Terminologies Page
st.title("Machine Learning Terminologies")

# Introduction
st.write("""
In machine learning, we use many terms. Let’s go through some of the key terms with simple examples that will help you understand them better.
""")

# Terminology 1: Algorithm
st.header("1. Algorithm")
st.write("""
An **algorithm** is like a recipe or set of instructions that helps the computer solve a problem.
- **Example**: If you're trying to sort your toys by size, you follow a set of instructions. Similarly, a sorting algorithm helps a computer sort things in a certain order, like arranging numbers from smallest to largest.
""")

# Terminology 2: Training Data
st.header("2. Training Data")
st.write("""
**Training data** is like a practice set where the computer learns how to make decisions.
- **Example**: Imagine you're learning to recognize animals. If you’re shown pictures of cats and dogs with labels (cat or dog), you’ll learn to tell the difference. The pictures are your training data!
""")

# Terminology 3: Testing Data
st.header("3. Testing Data")
st.write("""
**Testing data** is used to see if the computer learned well from the training data.
- **Example**: After learning to recognize cats and dogs, you get new pictures that you haven’t seen before. These new pictures are your testing data, and they help check if you really learned the difference between cats and dogs.
""")

# Terminology 4: Features
st.header("4. Features")
st.write("""
**Features** are the important parts of the data that help the computer make predictions.
- **Example**: Imagine you want to predict if a fruit is an apple or a banana. The **features** could be things like the fruit’s color, size, or shape. These features help the computer decide if the fruit is an apple or a banana.
""")

# Terminology 5: Model
st.header("5. Model")
st.write("""
A **model** is what the computer builds after learning from the data. It helps the computer make predictions.
- **Example**: After seeing enough pictures of cats and dogs, the computer builds a model that can help it predict if a new picture shows a cat or a dog, even if it has never seen that picture before.
""")
# Summary
st.header("In Summary:")
st.write("""
- **Algorithm**: A recipe of instructions.
- **Training Data**: The practice set used to learn.
- **Testing Data**: New data used to check if learning was correct.
- **Features**: Important parts of the data that help make decisions.
- **Model**: What the computer builds to make predictions after learning.
""")