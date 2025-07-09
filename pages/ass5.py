import streamlit as st
import pandas as pd

# Load the data
melbourn = pd.read_csv(r'C:\Users\user\Desktop\pandas\Melbourne_housing_FULL.csv')

st.title("Melbourne Housing Market Explorer")

# Display the data
st.subheader("Raw Data")
st.dataframe(melbourn.head(20))

# Dropdown to select numeric column
numeric_cols = melbourn.select_dtypes(include='number').columns.tolist()
selected_col = st.selectbox("Select a column to visualize", numeric_cols)

# Show histogram
st.subheader(f"Histogram of {selected_col}")
st.bar_chart(melbourn[selected_col].dropna())

# Summary statistics
st.subheader("Summary Statistics")
st.write(melbourn[selected_col].describe())
