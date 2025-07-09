import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🇳🇬 Nigeria Data Dashboard")

# File paths
lgas_file = r"C:\streamlit2\my_App\pages\list_of_local_government_areas_of_nigeria.csv"
states_file = r"C:\streamlit2\my_App\pages\list-states-nigeria-227j.csv"
poverty_lga_file = r"C:\streamlit2\my_App\pages\Nigeria povertyrate per local gov.csv"
poverty_state_file = r"C:\streamlit2\my_App\pages\poverty_nga.csv"

# Load data
lgas_df = pd.read_csv(lgas_file)
states_df = pd.read_csv(states_file)
poverty_lga_df = pd.read_csv(poverty_lga_file)
poverty_state_df = pd.read_csv(poverty_state_file)

# Show overview
st.header("📋 Raw Datasets Overview")
st.subheader("Local Government Areas")
st.dataframe(lgas_df)

st.subheader("States List")
st.dataframe(states_df)

st.subheader("Poverty Rate by LGA")
st.dataframe(poverty_lga_df)

st.subheader("Poverty Rate by State")
st.dataframe(poverty_state_df)

# Optional: Add state selector
st.header("🔍 Explore Poverty Data by State")

selected_state = st.selectbox("Choose a State", poverty_state_df['states'].unique())

filtered_lgas = poverty_lga_df[poverty_lga_df['states'] == selected_state]
st.subheader(f"Poverty Rate in LGAs of {selected_state}")
st.dataframe(filtered_lgas)

# Optional: Add chart
st.subheader(f"📊 Bar Chart of Poverty Rate in {selected_state}")
if 'poverty_rate' in filtered_lgas.columns:
    st.bar_chart(filtered_lgas.set_index('lga')['poverty_rate'])
else:
    st.warning("Column 'poverty_rate' not found in dataset.")
