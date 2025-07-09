import streamlit as st
import numpy as np
import pandas as pd
# # st.title("📈 Assignment 2 Visualization")

# # st.write("Here you can add all your pandas data analysis and charts!")

# # --- Dataset 2: Student Performance Metrics ---
# np.random.seed(101)
# n2 = 150
# subjects = ['Math', 'Science', 'English']
# grades = ['Primary 5', 'Primary 6', 'JSS1']
# genders = ['Male', 'Female']

# student_data = pd.DataFrame({
#     'StudentID': ['S' + str(i).zfill(3) for i in range(1, n2+1)],
#     'Gender': np.random.choice(genders, n2),
#     'Subject': np.random.choice(subjects, n2),
#     'Score': np.random.randint(30, 100, size=n2),
#     'StudyHours': np.round(np.random.normal(3, 1.5, size=n2), 1),
#     'GradeLevel': np.random.choice(grades, n2)
# })

# student_data.to_csv("student_scores.csv", index=False)

# print("✅ Datasets generated: drone_deliveries.csv & student_scores.csv")

# # pages/ass2.py
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.title("🎓 Student Score Dashboard")
# st.write("Explore academic performance based on study time, subject, and grade level.")

# # Load data
# @st.cache_data
# def load_data():
#     return pd.read_csv("student_scores.csv")

# df = load_data()

# # Show data
# if st.checkbox("📄 Show Student Data"):
#     st.dataframe(df)

# # Score Distribution by Subject
# st.subheader("📊 Score Distribution by Subject")
# fig1, ax1 = plt.subplots()
# sns.boxplot(data=df, x="Subject", y="Score", palette="Set2", ax=ax1)
# st.pyplot(fig1)

# # Study Time vs Score
# st.subheader("📚 Study Hours vs Score")
# fig2, ax2 = plt.subplots()
# sns.scatterplot(data=df, x="StudyHours", y="Score", hue="Gender", ax=ax2)
# st.pyplot(fig2)

# # Average Score by Grade Level
# st.subheader("🏫 Average Score by Grade Level")
# avg_scores = df.groupby("GradeLevel")["Score"].mean().reset_index()
# fig3, ax3 = plt.subplots()
# sns.barplot(data=avg_scores, x="GradeLevel", y="Score", ax=ax3)
# st.pyplot(fig3)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data1 = pd.read_csv(r"C:\Users\user\Desktop\pandas\MELBOURNE_HOUSE_PRICES_LESS.csv")

st.title("Melbourne House Prices Explorer")

# Show raw data
st.subheader("Dataset Preview")
st.dataframe(data1.head())

# Summary statistics
st.subheader("Summary Statistics")
st.write(data1.describe())

# Drop rows with missing 'Price' for visualizations
cleaned = data1.dropna(subset=['Price'])

# Histogram of Prices
st.subheader("Price Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(cleaned['Price'], bins=50, kde=True, ax=ax1)
st.pyplot(fig1)

# Top 10 Suburbs by Average Price
st.subheader("Top 10 Suburbs by Average Price")
if 'Suburb' in cleaned.columns:
    avg_price = cleaned.groupby('Suburb')['Price'].mean().sort_values(ascending=False).head(10)
    st.bar_chart(avg_price)

# Scatter Plot: Landsize vs Price
if 'Landsize' in cleaned.columns:
    st.subheader("Landsize vs Price")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=cleaned, x='Landsize', y='Price', alpha=0.5, ax=ax2)
    ax2.set_xlim(0, 1000)  # remove extreme outliers
    st.pyplot(fig2)

# Avg Price per Bedroom
if 'Bedroom2' in cleaned.columns:
    st.subheader("Average Price per Bedroom Count")
    bedroom_price = cleaned.groupby('Bedroom2')['Price'].mean()
    st.bar_chart(bedroom_price)



# st.set_page_config(page_title="Drone Dashboard", layout="wide")

# # Load data
# @st.cache_data
# def load_data():
#     return pd.read_csv("drone_deliveries.csv")

# df = load_data()

# st.title("🚁 Drone Delivery Dashboard")
# st.write("Explore performance metrics of drone deliveries across Nigerian cities.")

# # Sidebar filters
# st.sidebar.header("📍 Filter Deliveries")
# selected_city = st.sidebar.selectbox("Select City", options=["All"] + sorted(df["City"].unique().tolist()))
# selected_drone = st.sidebar.multiselect("Select Drone Model", options=sorted(df["DroneModel"].unique().tolist()), default=df["DroneModel"].unique())

# # Filter data
# filtered_df = df.copy()
# if selected_city != "All":
#     filtered_df = filtered_df[filtered_df["City"] == selected_city]
# if selected_drone:
#     filtered_df = filtered_df[filtered_df["DroneModel"].isin(selected_drone)]

# # Show data
# if st.checkbox("🔍 Show Filtered Data"):
#     st.dataframe(filtered_df)

# # Charts
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("⏱️ Delivery Time Distribution")
#     fig1, ax1 = plt.subplots()
#     sns.histplot(filtered_df["DeliveryTime (min)"], kde=True, ax=ax1, color='skyblue')
#     st.pyplot(fig1)

# with col2:
#     st.subheader("📦 Avg Package Weight by Drone Model")
#     fig2, ax2 = plt.subplots()
#     sns.barplot(data=filtered_df, x="DroneModel", y="PackageWeight (kg)", ax=ax2)
#     st.pyplot(fig2)

# # Success Rate
# st.subheader("✅ Success Rate by City")
# success_rate = filtered_df.groupby("City")["Successful"].mean().reset_index()
# fig3, ax3 = plt.subplots()
# sns.barplot(data=success_rate, x="City", y="Successful", ax=ax3)
# ax3.set_ylabel("Success Rate")
# st.pyplot(fig3)

