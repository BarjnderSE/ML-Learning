import streamlit as st

# Title for Libraries Page
st.title("Libraries We Are Going to Use")

# Introduction
st.write("""
In this project, we will be using several libraries essential for machine learning, data analysis, and computer vision. 
Below is the `pip install` command to install all the libraries at once.
""")

# Installation command in one line
st.write("""
To install all the required libraries, run the following command:
`pip install pandas numpy scikit-learn keras tensorflow torch spacy nltk opencv-python jupyter`
""")

# Overview of the Libraries
st.header("Overview of the Libraries:")
st.write("""
- **Pandas**: For data manipulation and analysis.
- **Numpy**: For numerical computing and handling arrays/matrices.
- **Scikit-Learn**: For machine learning algorithms and tools.
- **Keras**: For building deep learning models.
- **TensorFlow**: A framework for deep learning tasks.
- **PyTorch**: A flexible deep learning framework.
- **NLP**: Natural language processing tools like `spaCy` or `NLTK`.
- **OpenCV**: For image processing and computer vision tasks.
- **Jupyter Notebook**: An interactive environment for coding and sharing data.
""")
