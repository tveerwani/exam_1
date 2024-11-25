# Importing necessary libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="Automobile Data Analysis", layout="wide")

# Load dataset
url = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
@st.cache
def load_data():
    return pd.read_csv(url)

df = load_data()

# App Title
st.title("Automobile Data Analysis Dashboard")

# Show raw data
st.header("1. Raw Dataset")
if st.checkbox("Show raw data"):
    st.write(df)

# Correlation heatmap
st.header("2. Correlation Heatmap")
if st.checkbox("Show correlation heatmap"):
    st.subheader("Correlation between numerical features")
    corr_matrix = df.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Scatter plots
st.header("3. Scatter Plot Analysis")
option = st.selectbox(
    "Select a relationship to visualize",
    ["engine-size vs price", "highway-mpg vs price"]
)

if option == "engine-size vs price":
    st.subheader("Engine Size vs Price")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.regplot(x="engine-size", y="price", data=df, ax=ax)
    st.pyplot(fig)
elif option == "highway-mpg vs price":
    st.subheader("Highway-MPG vs Price")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.regplot(x="highway-mpg", y="price", data=df, ax=ax)
    st.pyplot(fig)

# Summary statistics
st.header("4. Summary Statistics")
if st.checkbox("Show summary statistics"):
    st.write(df.describe())

# Footer
st.markdown("### Created with ❤️ using Streamlit")
