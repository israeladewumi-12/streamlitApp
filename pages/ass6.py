import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"./pages/Nigeria_Debt_Servicing_Percentage_1999_2024.csv"
df = pd.read_csv(file_path)

# App title
st.title("🇳🇬 Nigeria Debt Servicing as % of Revenue (1999–2024)")

# Display the raw data
st.subheader("Raw Data")
st.dataframe(df)

# Line chart visualization
st.subheader("Debt Servicing (% of Revenue) Over the Years")
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Debt_Servicing_Percentage'], marker='o', color='crimson')
ax.set_xlabel("Year")
ax.set_ylabel("Debt Servicing (%)")
ax.set_title("Nigeria's Debt Servicing Trend (1999–2024)")
ax.grid(True)
st.pyplot(fig)

# Optional: summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())
