import streamlit as st
st.title("Types of Machine Learning")
# Add Tabs for Each ML Type
tab1, tab2, tab3, tab4 = st.tabs(["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Semi-Supervised Learning"])

# Supervised Learning
with tab1:
    st.header("Supervised Learning")
    st.write("""
    In supervised learning, the model learns from labeled data, meaning the input data is paired with the correct output.
    - **Example**: Predicting house prices based on features like size, location, and number of rooms.
    """)

# Unsupervised Learning
with tab2:
    st.header("Unsupervised Learning")
    st.write("""
    Unsupervised learning involves training the model on data without labels. The model tries to find patterns or groupings on its own.
    - **Example**: Grouping customers into segments based on purchasing behavior.
    """)

# Reinforcement Learning
with tab3:
    st.header("Reinforcement Learning")
    st.write("""
    In reinforcement learning, the model learns by interacting with an environment and receiving rewards or penalties for its actions.
    - **Example**: Teaching a robot to walk by rewarding it for stable movements.
    """)

# Semi-Supervised Learning
with tab4:
    st.header("Semi-Supervised Learning")
    st.write("""
    Semi-supervised learning is a combination of supervised and unsupervised learning. The model is trained on a small amount of labeled data and a large amount of unlabeled data. It helps in cases where labeling data is expensive or time-consuming.
    
    - **Example**: Imagine a medical dataset with a few labeled images of tumors and many unlabeled images. The model can use the labeled data to understand patterns and then apply this knowledge to the unlabeled data to improve predictions.
    """)

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Semi-Supervised_Learning_Concept.svg/500px-Semi-Supervised_Learning_Concept.svg.png", 
        caption="Semi-Supervised Learning Example", 
        use_container_width=True
    )


# Closing Note
st.write("""
These categories form the foundation of Machine Learning. Explore each to understand how machines learn and apply them in real-world scenarios!
""")
