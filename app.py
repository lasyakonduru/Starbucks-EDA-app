# YOUR APP HERE!
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title = "Starbucks EDA App", layout = "wide", page_icon= "☕")

df = pd.read_csv("data/cleaned_starbucks.csv")

# Navigation bar
st.sidebar.title("☕ The Starbucks EDA App")
page = st.sidebar.radio("🌟 Go to:", ["🏠 Home", "📊 Data Overview", "📈 EDA"])

# Home Page
if page == "🏠 Home":
    st.title("☕ Welcome to the Starbucks Nutrition Explorer!")
    st.image("Starbucks-logo.png", width = 300)
    st.markdown("""
    ### 👋 Hello!
    Welcome to this interactive app that helps you explore Starbucks' nutritional facts with ease.
    
    ---
    
    🔍 **What You Can Do:**
    - 🍩 Discover insights on calories, fat, sugar, and caffeine
    - 📊 Visualize distributions and patterns using histograms, boxplots, and scatterplots
    - ⚙️ Filter data by beverage category and nutritional ranges
    - 📁 Navigate between different sections using the **sidebar**
    
    ---
    
    ✨ **Why This App?**
    
    Whether you're a **health-conscious customer**, a **data analyst**, or just **curious about your favorite drink**, this app gives you a clear look at what’s inside those Starbucks cups ☕.
    
    ✅ Powered by **Python + Streamlit**
    """)
    st.balloons()

# Data Overview
elif page == "📊 Data Overview":
    st.header("📋 Starbucks Dataset Overview")
    st.write("Below is a sample of the dataset:")
    st.dataframe(df.head())

    st.markdown("### 🔍 Feature Info:")
    st.markdown("""
    This dataset contains the **nutritional information for various Starbucks menu items**. It's a clean and structured dataset designed to help analyze the health-related aspects of Starbucks beverages.
    
    - **`Beverage_category`**: Broad classification of drinks (e.g., coffee, tea, smoothie).
    - **`Beverage`**: Specific drink names (e.g., *Caramel Macchiato*, *Green Tea Latte*).
    - **`Beverage_prep`**: Preparation method (e.g., hot, iced, with whipped cream, etc.).
    - **`Calories`**: Total energy in each beverage.
    - **`Total Fat (g)`, `Trans Fat (g)`, `Saturated Fat (g)`**: Breakdown of fat content — important for dietary and heart health considerations.
    - **`Sodium (mg)`**: Sodium levels, crucial for low-sodium diets.
    - **`Total Carbohydrates (g)`**: Includes sugars and starches — especially useful for people with diabetes or low-carb diets.
    - **`Cholesterol (mg)`**: Amount of cholesterol — relevant for heart health monitoring.
    
    This dataset is especially valuable for:
    - 🧪 **Researchers** looking at trends in food and nutrition
    - 🥗 **Dietitians** analyzing intake patterns
    - 💪 **Health-conscious consumers** tracking their dietary choices
    
    It provides an excellent foundation for conducting EDA and developing interactive data applications using tools like Streamlit.
    """)
    st.markdown("### Columnal Information")
    info_df = pd.DataFrame({
        "Column Name": df.columns,
        "Non-Null Count": df.notnull().sum().values,
        "Data Type": df.dtypes.values
    })
    st.dataframe(info_df)
    
    st.markdown(f"**Number of Entries:** {len(df)}")
    st.markdown(f"**Number of Unique Beverages:** {df['Beverage'].nunique()}")
    
    st.markdown("📂 For more info on the dataset: [View Dataset Source](https://www.kaggle.com/datasets/starbucks/starbucks-menu)")

# EDA Page
elif page == "📈 EDA":
    st.title("📈 Exploratory Data Analysis (EDA)")
    st.markdown("""
    Welcome to the **Exploratory Data Analysis** page! This is the FUN part of this app!!
    Here, you can interactively explore the Starbucks dataset to uncover insights about beverage nutrition.
    
    Use the filters to narrow down the data by beverage category or calorie range.  
    Visualize patterns, compare variables, and better understand what's behind your favorite Starbucks drinks.
    
    You can explore:
    - **Histograms** to see how data is distributed.
    - **Scatter Plots** to explore relationships between variables.
    - **Box Plots** to check for outliers and variability.
    
    Scroll down and play with the plots! ☕📊
    """)

    numeric_cols = df.select_dtypes(include = 'number').columns.tolist()

    # Optional filter: Beverage category
    if 'Beverage_category' in df.columns:
        category_filter = st.multiselect("Filter by Beverage Category (optional)", df['Beverage_category'].unique())
        if category_filter:
            df = df[df['Beverage_category'].isin(category_filter)]

    # Optional filter: Calories slider
    if 'Calories' in df.columns:
        min_cal, max_cal = st.slider("Select Calorie Range (optional)", 
                                     int(df["Calories"].min()), 
                                     int(df["Calories"].max()), 
                                     (int(df["Calories"].min()), int(df["Calories"].max())))
        df = df[(df["Calories"] >= min_cal) & (df["Calories"] <= max_cal)]

    st.markdown("### 📊 Histogram")
    col1 = st.selectbox("Choose a column for histogram", numeric_cols)
    fig, ax = plt.subplots(figsize = (4, 3))
    sns.histplot(df[col1], kde = True, ax = ax)
    st.pyplot(fig)

    st.markdown("### 🟢 Scatter Plot")
    x_axis = st.selectbox("X-axis", numeric_cols, key ="x_axis")
    y_axis = st.selectbox("Y-axis", numeric_cols, key ="y_axis")
    fig2, ax2 = plt.subplots(figsize = (4, 3))
    sns.scatterplot(x = df[x_axis], y = df[y_axis], ax = ax2)
    st.pyplot(fig2)

    st.markdown("### 📦 Box Plot")
    col2 = st.selectbox("Choose a column for box plot", numeric_cols, key = "box_col")
    fig3, ax3 = plt.subplots(figsize = (4, 3))
    sns.boxplot(y = df[col2], ax = ax3)
    st.pyplot(fig3)
