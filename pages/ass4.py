import streamlit as st
import pandas as pd

# Load the dataset
melbourn = pd.read_csv(r'./pages/Melbourne_housing_FULL.csv')

st.title("Melbourne Housing Dataset Explorer")

# Show basic info
st.subheader("Preview of Data")
st.write(melbourn.head())

# Choose column to visualize
st.subheader("Choose a Feature to Visualize")
column = st.selectbox("Select numeric column", melbourn.select_dtypes(include='number').columns)

# Plot a histogram of the selected column
st.subheader(f"Histogram of {column}")
st.bar_chart(melbourn[column].dropna())

# Optional: Filter by suburb
if 'Suburb' in melbourn.columns:
    st.subheader("Filter by Suburb")
    suburb = st.selectbox("Choose a Suburb", melbourn['Suburb'].dropna().unique())
    st.write(melbourn[melbourn['Suburb'] == suburb])

# Show basic stats
st.subheader("Summary Statistics")
st.write(melbourn.describe())
