import streamlit as st

# Title
st.title("Data Preprocessing Overview")

# Section 1: Data Cleaning
st.header("1. Data Cleaning")
st.write("""
- **Tidy Data:** Ensures each variable is a column and each observation a row.
- **Missing Values:** Handle missing data through removal or imputation.
- **Outliers:** Detect and manage outliers to maintain data quality.
""")

# Section 2: Data Integration
st.header("2. Data Integration")
st.write("""
- **Combining Data Sources:** Integrate databases for a unified dataset.
- **Example:** Merging sales data from various regions.
""")

# Section 3: Data Transformation
st.header("3. Data Transformation")
st.write("""
- **Scaling:** Normalize or standardize data for model readiness.
- **Aggregation:** Summarize data (e.g., average sales).
- **Generalization:** Reduce detail level (e.g., age groups).
- **Grouping:** Subset data based on criteria.
- **Hierarchical Structures:** Organize data in tree-like formats.
""")

# Section 4: Data Reduction
st.header("4. Data Reduction")
st.write("""
- **Dimensional Reduction:** Use PCA to reduce feature count.
- **Numerical Reduction:** Simplify numerical data.
- **Compression:** Techniques to minimize data size.
""")

# Section 5: Data Discretization
st.header("5. Data Discretization")
st.write("""
- Convert continuous data into discrete categories for easier analysis.
""")

# Summary
st.header("Summary")
st.write("Data preprocessing is essential for preparing datasets for analysis and ensuring high-quality inputs for machine learning models.")