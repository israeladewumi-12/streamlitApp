
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r'C:\streamlit2\my_App\california_cities.csv')
data.info()


# Load the data
data = pd.read_csv(r'C:\streamlit2\my_App\california_cities.csv')

# Set the page title
st.title("California Cities Data Viewer")

# Show basic information
st.subheader("Dataset Overview")
st.write(f"Shape of data: {data.shape}")
st.write("First 5 rows of the dataset:")
st.dataframe(data.head())

# Show data summary
st.subheader("Summary Statistics")
st.write(data.describe())

# Optional: Select columns to view
st.subheader("Choose columns to display")
selected_columns = st.multiselect("Select columns:", data.columns.tolist(), default=data.columns.tolist())
st.dataframe(data[selected_columns])

# Optional: Filter by population
st.subheader("Filter by Minimum Population")
min_pop = st.slider("Minimum population", int(data["population_total"].min()), int(data["population_total"].max()), 50000)
filtered_data = data[data["population_total"] >= min_pop]
st.write(f"Cities with population >= {min_pop}:")
st.dataframe(filtered_data)

# Visualizations
st.subheader("Population Distribution")
st.bar_chart(data['population_total'])

# # # --- Dataset 1: Drone Delivery Logs ---
# # np.random.seed(42)r
# # n1 = 200
# # cities = ['Lagos', 'Abuja', 'Ibadan', 'Kano', 'Port Harcourt']
# # drones = ['FalconX', 'SwiftBee', 'SkyMax', 'AirXpress']

# # drone_data = pd.DataFrame({
# #     'DeliveryID': ['D' + str(i).zfill(4) for i in range(1, n1+1)],
# #     'City': np.random.choice(cities, n1),
# #     'DeliveryTime (min)': np.random.normal(loc=30, scale=10, size=n1).astype(int),
# #     'PackageWeight (kg)': np.round(np.random.uniform(0.5, 5.0, n1), 2),
# #     'DroneModel': np.random.choice(drones, n1),
# #     'Successful': np.random.choice([True, False], n1, p=[0.9, 0.1])
# # })

# # drone_data.to_csv("drone_deliveries.csv", index=False)

# # # Layout.py
# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns

# # # Page Setup
# # st.title("🚁 Drone Delivery Dashboard")
# # st.write("Explore performance metrics of drone deliveries across Nigerian cities.")

# # # Load data
# # @st.cache_data
# # def load_data():
# #     return pd.read_csv("drone_deliveries.csv")

# # df = load_data()

# # # Show data
# # if st.checkbox("🔍 Show Raw Data"):
# #     st.dataframe(df)

# # # Delivery Time Distribution
# # st.subheader("⏱️ Delivery Time Distribution")
# # fig1, ax1 = plt.subplots()
# # sns.histplot(df["DeliveryTime (min)"], kde=True, ax=ax1, color='skyblue')
# # st.pyplot(fig1)

# # # Success Rate by City
# # st.subheader("✅ Success Rate by City")
# # success_rate = df.groupby("City")["Successful"].mean().reset_index()
# # fig2, ax2 = plt.subplots()
# # sns.barplot(data=success_rate, x="City", y="Successful", ax=ax2)
# # ax2.set_ylabel("Success Rate")
# # st.pyplot(fig2)

# # # Average Delivery Time per Drone Model
# # st.subheader("🚀 Avg Delivery Time per Drone Model")
# # avg_time = df.groupby("DroneModel")["DeliveryTime (min)"].mean().reset_index()
# # fig3, ax3 = plt.subplots()
# # sns.barplot(data=avg_time, x="DroneModel", y="DeliveryTime (min)", ax=ax3)
# # st.pyplot(fig3)





# st.set_page_config(page_title="Student Dashboard", layout="wide")

# # Load data
# @st.cache_data
# def load_data():
#     return pd.read_csv("student_scores.csv")

# df = load_data()

# st.title("🎓 Student Score Dashboard")
# st.write("Explore academic performance based on study time, subject, and grade level.")

# # Sidebar filters
# st.sidebar.header("📊 Filter Students")
# selected_subject = st.sidebar.selectbox("Subject", options=["All"] + sorted(df["Subject"].unique().tolist()))
# selected_grade = st.sidebar.multiselect("Grade Level", options=sorted(df["GradeLevel"].unique().tolist()), default=df["GradeLevel"].unique())
# selected_gender = st.sidebar.radio("Gender", options=["All", "Male", "Female"])

# # Apply filters
# filtered_df = df.copy()
# if selected_subject != "All":
#     filtered_df = filtered_df[filtered_df["Subject"] == selected_subject]
# if selected_grade:
#     filtered_df = filtered_df[filtered_df["GradeLevel"].isin(selected_grade)]
# if selected_gender != "All":
#     filtered_df = filtered_df[filtered_df["Gender"] == selected_gender]

# # Show filtered data
# if st.checkbox("📄 Show Filtered Student Data"):
#     st.dataframe(filtered_df)

# # Charts
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("📈 Score Distribution")
#     fig1, ax1 = plt.subplots()
#     sns.histplot(filtered_df["Score"], bins=20, kde=True, ax=ax1, color='green')
#     st.pyplot(fig1)

# with col2:
#     st.subheader("📚 Study Hours vs Score")
#     fig2, ax2 = plt.subplots()
#     sns.scatterplot(data=filtered_df, x="StudyHours", y="Score", hue="Gender", ax=ax2)
#     st.pyplot(fig2)

# # Average Score by Grade
# st.subheader("🏫 Average Score by Grade Level")
# avg_scores = filtered_df.groupby("GradeLevel")["Score"].mean().reset_index()
# fig3, ax3 = plt.subplots()
# sns.barplot(data=avg_scores, x="GradeLevel", y="Score", ax=ax3)
# st.pyplot(fig3)
