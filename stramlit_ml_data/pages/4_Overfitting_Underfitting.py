import streamlit as st

# Title for Overfitting and Underfitting Explanation Page
st.title("Overfitting and Underfitting in Machine Learning")

# Introduction
st.write("""
In machine learning, two common problems that can occur when building a model are **overfitting** and **underfitting**. 
Both problems happen when the model doesn't generalize well to new, unseen data. Let's break down what these terms mean and what you can do to prevent them.
""")

# Overfitting Explanation
st.header("1. Overfitting")

st.write("""
**Overfitting** happens when a model learns the training data too well, to the point where it starts to memorize the details rather than learning the underlying patterns. 

While this may lead to excellent performance on the training data, the model performs poorly on new, unseen data because it can't generalize well.

**Example**: Imagine you're trying to predict the shirt size of a person based on their height and weight. If the model overfits, it might memorize the exact height and weight for each person in the training data and make predictions based on those specific values. If you then show it new data with slightly different measurements, the model won’t perform well, as it has only memorized the training data instead of learning general relationships.

### What to Do to Avoid Overfitting:
- **Use more data**: The more data the model sees, the better it can generalize.
- **Simplify the model**: Avoid using a very complex model that tries to fit every tiny detail.
- **Apply regularization**: Regularization techniques like L1 or L2 help prevent the model from becoming too complex.
  
### What Not to Do:
- Don’t let the model memorize specific examples.
- Don’t use too little data.
""")

# Underfitting Explanation
st.header("2. Underfitting")

st.write("""
**Underfitting** happens when the model is too simple to capture the underlying patterns in the data. It fails to learn well even from the training data, leading to poor performance both on the training and unseen data.

**Example**: In the shirt size prediction example, if the model only considers one feature (like height) and ignores weight, it may not capture enough information to make accurate predictions. This leads to underfitting because the model is too simple to understand the relationship between height, weight, and shirt size.

### What to Do to Avoid Underfitting:
- **Use a more complex model**: Choose a model that can learn from the data’s complexity.
- **Add more features**: Include relevant features (e.g., height, weight, body type) that will help the model understand better.
  
### What Not to Do:
- Don’t make the model too simple.
- Don’t ignore important data points that could help in making predictions.
""")

# Shirt Size Example: Overfitting and Underfitting
st.header("Shirt Size Example Clarification")

st.write("""
### Overfitting:
If the model memorizes the height and weight exactly from the training data (e.g., a specific person’s height and weight always maps to a specific shirt size), it won’t generalize well to new, unseen data. In this case, the same height or weight might correspond to a different shirt size in real-world situations, but the overfitted model won’t handle that correctly because it has only memorized the training examples.

### Underfitting:
If the model only uses height as a feature to predict shirt size, it’s too simple to capture the full relationship between height, weight, and shirt size. It’s missing important information (like weight) that would help it make better predictions. As a result, it will fail to make accurate predictions even on the training data.
""")

# Summary of Best Approaches
st.header("In Summary:")

st.write("""
- **For Overfitting**:
  - **Do**: Use more data, simplify the model, and apply regularization.
  - **Don’t**: Let the model memorize data, or use too little data.
  
- **For Underfitting**:
  - **Do**: Use a more complex model, and include more relevant features.
  - **Don’t**: Make the model too simple, or ignore important features.
""")
st.write("This summary should help you understand how to approach overfitting and underfitting in general and more relevant features")