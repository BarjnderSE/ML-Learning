import streamlit as st

# Title for the page
st.title("Data Preprocessing Steps")

# Introduction
st.write("""
Data preprocessing is a crucial part of the machine learning pipeline. It involves cleaning, transforming, and organizing the data to make it suitable for analysis and model building.
Let's walk through the essential data preprocessing steps.
""")

# 1. Data Cleaning
st.header("1. Data Cleaning")

st.subheader("Tidy Data Cleaning")
st.write("""
Tidy data refers to a format in which each variable is represented by a column, and each observation is represented by a row. This format makes it easier to work with data and perform analysis.
""")

st.subheader("Handling Missing Values")
st.write("""
Missing values can be handled in several ways:
- Removing rows or columns with missing values.
- Imputing missing values (e.g., using the mean, median, or mode).
""")

st.subheader("Handling Outliers")
st.write("""
Outliers are extreme values that might distort the analysis. You can handle outliers by:
- Identifying them using statistical methods (e.g., IQR method).
- Removing or replacing them with more appropriate values.
""")

# 2. Data Integration (or Data Pooling)
st.header("2. Data Integration (or Data Pooling)")

st.write("""
Data integration involves combining data from different sources into one unified dataset. This allows us to work with all available data in one place.
Example:
- Combining customer data and their purchase history into a single dataset for analysis.
""")


import streamlit as st

# Data Transformation Section
st.header("3. Data Transformation")

# Data Scaling
st.subheader("Data Scaling")
st.write("""
    Scaling ensures that all features are on the same scale. Common methods include:

    - **Standardization**: This technique involves adjusting the data to have a zero mean and unit variance.
    - **Normalization**: This method rescales the values of the features to fall within a specific range, typically between 0 and 1.
""")

# Example for Standardization
st.subheader("Example for Standardization")
st.write("""
    Standardization is done by subtracting the mean of each feature and dividing by the standard deviation:
    
    $$ X_{standardized} = \frac{X - \mu}{\sigma} $$

    Where:
    - X is the original feature value
    - μ is the mean
    - σ is the standard deviation
""")

# Data Aggregation
st.subheader("Data Aggregation")
st.write("""
    Aggregation involves combining multiple rows of data into a single summary. For example, summing daily sales to get monthly totals.
""")

# Grouping of Data
st.subheader("Grouping of Data")
st.write("""
    Grouping data means organizing it into sets of similar observations. For example, grouping sales data by region to perform regional analysis.
""")

# Hierarchical Data
st.subheader("Hierarchical Data")
st.write("""
    Hierarchical data is structured in a tree-like manner. For example, product categories and their respective subcategories.
""")

# Data Reduction Section
st.header("4. Data Reduction")

# Dimensionality Reduction
st.subheader("Dimensionality Reduction")
st.write("""
    Dimensionality reduction techniques like **Principal Component Analysis (PCA)** help reduce the number of features while retaining important information, making the data more manageable.
""")

# Example for PCA
st.subheader("Example for PCA")
st.write("""
    PCA reduces the data by transforming the original features into a new set of features (principal components) that capture the most variance in the data.
    
    - PCA helps in visualizing high-dimensional data.
    - It allows faster processing and reduced storage needs.
""")

# Data Compression
st.subheader("Data Compression")
st.write("""
    Data compression reduces the size of the data for efficient storage and faster processing. This can be done through various encoding techniques.
""")

# Data Discretization Section
st.header("5. Data Discretization")

# Discretization
st.write("""
    Discretization converts continuous data into categorical intervals. This is useful for models like decision trees, which work better with discrete data. 
    Example: Converting age into categories like 'young', 'middle-aged', and 'old'.
""")

# Example for Discretization
st.subheader("Example for Discretization")
st.write("""
    A common example of discretization is converting continuous age values into categories:

    - Age: 18-25 -> 'young'
    - Age: 26-40 -> 'middle-aged'
    - Age: 41+ -> 'old'
""")

# Summary Section
st.header("Summary of Preprocessing Steps")

st.write("""
    Here is a quick summary of the preprocessing steps:

    1. **Data Cleaning**: Fix missing values, remove or treat outliers, and tidy the data.
    2. **Data Integration**: Combine data from different sources into one dataset.
    3. **Data Transformation**: Scale data, normalize, and aggregate to make it ready for analysis.
    4. **Data Reduction**: Reduce the number of features or compress the data for efficiency.
    5. **Data Discretization**: Convert continuous data into categories for easier modeling.
""")
