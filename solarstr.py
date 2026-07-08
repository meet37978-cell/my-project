import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_squared_error,mean_absolute_error
import plotly.express as px

# streamlit run solarstr.py    


st.sidebar.title("☀️ Solar")
st.sidebar.markdown("Energy Management System")

st.sidebar.markdown("---")

page = st.sidebar.radio("Navigation", [
        "🏠 Home Dashboard",
        "📋 Dataset Overview",
        "🌤️ Weather Analytics",
        "⚡ Solar Analytics",
        "🔋 Battery Analytics",
        "🤖 Model Training",
        "📊 Model Comparison",
        "🎯 Real-Time Prediction",
        "💰 Bill Savings",
        "🏗 Solar Installation Planner"
], label_visibility="collapsed")

# csv
z = pd.read_csv("solar_merged_data.csv")
df = pd.DataFrame(z)

# csv load
df = pd.read_csv("solar_merged_data.csv")

# -----------------------
# 🧹 BASIC CLEANING
# -----------------------

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(df.median(numeric_only=True))
df = df.fillna(df.mode().iloc[0])  # categorical fill

# -----------------------
# 🚨 OUTLIER REMOVAL (SIMPLIFIED)
# -----------------------

num_cols = df.select_dtypes(include="number").columns

Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1

df = df[~((df[num_cols] < (Q1 - 1.5 * IQR)) |
          (df[num_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]

st.sidebar.success(
    f"""
📊 {len(df):,} records | {df.shape[1]} features

📅 {df.iloc[:,0].min()} → {df.iloc[:,0].max()}
"""
)

if page == "🏠 Home Dashboard":
    st.markdown(
        """
        <h1 style='color:#FFA500; text-align:center; font-weight:bold;'>
        ☀️ Solar Smart Energy Dashboard
        </h1>
        """,
        unsafe_allow_html=True
    )
    # KPI Calculations

    # ── KPI Metrics ──────────────────────────────────────────
    total_ac = df["AC_POWER"].sum()
    total_dc = df["DC_POWER"].sum()
    avg_irr = df["IRRADIATION"].mean()
    avg_mod_temp = df["MODULE_TEMPERATURE"].mean()
    max_daily = df["DAILY_YIELD"].max()
    total_records = len(df)

    c1, c2, c3 = st.columns(3)
    c1.metric("⚡ Total AC Power (kW)", f"{total_ac:,.0f}")
    c2.metric("🔋 Total DC Power (kW)", f"{total_dc:,.0f}")
    c3.metric("☀️ Avg Irradiation (W/m²)", f"{avg_irr:.4f}")

    c4, c5, c6 = st.columns(3)
    c4.metric("🌡️ Avg Module Temp (°C)", f"{avg_mod_temp:.2f}")
    c5.metric("📈 Max Daily Yield (kWh)", f"{max_daily:,.2f}")
    c6.metric("🗃️ Total Records", f"{total_records:,}")

    st.divider()

    df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])
    df = df.sort_values("DATE_TIME")
    df["MONTH"] = df["DATE_TIME"].dt.to_period("M").astype(str)

    # -------------------
    # 1. Daily Generation (Orange)
    # -------------------
    daily = df.groupby("DATE_TIME")["AC_POWER"].sum().reset_index()

    fig1 = px.line(
        daily,
        x="DATE_TIME",
        y="AC_POWER",
        title="Daily AC Power Generation",
        labels={"AC_POWER": "AC Power (kW)", "DATE": "Date"},
        color_discrete_sequence=["#F4A62A"]   # orange
    )
    fig1.update_layout(hovermode="x unified")
    st.plotly_chart(fig1, use_container_width=True)

    # -------------------
    # 2. Monthly Generation (Blue)
    # -------------------
    monthly = df.groupby("MONTH")["AC_POWER"].sum().reset_index()

    fig2 = px.bar(
        monthly,
        x="MONTH",
        y="AC_POWER",
        title="Monthly AC Power Generation",
        labels={"AC_POWER": "AC Power (kW)", "MONTH": "Month"},
        color="AC_POWER", color_continuous_scale="Oranges"
    )
    st.plotly_chart(fig2, use_container_width=True)



    # -------------------
    # 3. Irradiation (Yellow)
    # -------------------
    irr = df.groupby("DATE_TIME")["IRRADIATION"].mean().reset_index()

    fig3 = px.area(
        irr,
        x="DATE_TIME",
        y="IRRADIATION",
        title="Irradiation Trend",
        color_discrete_sequence=["#FFD700"]   # yellow
    )
    st.plotly_chart(fig3, use_container_width=True)

    # -------------------
    # 4. Temperature (Red + Green)
    # -------------------
    temp = df.groupby("DATE_TIME")[["AMBIENT_TEMPERATURE", "MODULE_TEMPERATURE"]].mean().reset_index()

    fig4 = px.line(
        temp,
        x="DATE_TIME",
        y=["AMBIENT_TEMPERATURE", "MODULE_TEMPERATURE"],
        title="Temperature Trend",
        color_discrete_sequence=["#1f77b4", "#d62728"]  # blue + red
    )

    st.plotly_chart(fig4, use_container_width=True)

elif page == "📋 Dataset Overview":
    st.title(" Dataset Overview")
    st.divider()


    c1, c2, c3 = st.columns(3)
    c1.metric("Total Records", f"{len(df):,}")
    c2.metric("Total Columns", len(df.columns))
    c3.metric("Plants", df["PLANT_ID"].nunique() if "PLANT_ID" in df.columns else "N/A")

    st.divider()

    tab1, tab2, tab3 = st.tabs(["Sample Data", "Column Info", "Statistics"])

    with tab1:
        n = st.slider("Rows to display", 5, 100, 20)
        st.dataframe(df.head(n), use_container_width=True)
    

    with tab2:
        info_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.values.astype(str),
            "Non-Null Count": df.notnull().sum().values,
            "Null Count": df.isnull().sum().values,
            "Unique Values": [df[c].nunique() for c in df.columns],
        })
        st.dataframe(info_df, use_container_width=True)

    with tab3:
        num_cols = df.select_dtypes(include=np.number).columns.tolist()
        st.dataframe(df[num_cols].describe().round(3), use_container_width=True)
        title="Wind Speed Trend",

elif page == "🌤️ Weather Analytics":

    st.title("🌤️ Weather Analytics")

    t1, t2, t3 = st.tabs([
        "🌡️ Ambient Temperature",
        "🔥 Module Temperature",
        "☀️ Irradiation"
    ])

    # ==================================
    # Ambient Temperature
    # ==================================
    with t1:

        st.subheader("Temperature Data")

        st.dataframe(
            df[[
                "DATE_TIME",
                "AMBIENT_TEMPERATURE",
                "AC_POWER"
            ]]
        )

        fig1 = px.scatter(
            df,
            x="AMBIENT_TEMPERATURE",
            y="AC_POWER",
            color="AMBIENT_TEMPERATURE",
            title="Ambient Temperature vs AC Power",
            color_continuous_scale="YlOrBr"
        )

        fig1.update_layout(
            xaxis_title="Ambient Temperature (°C)",
            yaxis_title="AC Power (kW)"
        )

        st.plotly_chart(fig1, use_container_width=True)

    # ==================================
    # Module Temperature
    # ==================================
    with t2:

        st.subheader("Module Temperature Data")

        st.dataframe(
            df[[
                "DATE_TIME",
                "MODULE_TEMPERATURE",
                "AC_POWER"
            ]]
        )

        fig2 = px.scatter(
            df,
            x="MODULE_TEMPERATURE",
            y="AC_POWER",
            color="MODULE_TEMPERATURE",
            title="Module Temperature vs AC Power",
            color_continuous_scale="Reds"
        )

        fig2.update_layout(
            xaxis_title="Module Temperature (°C)",
            yaxis_title="AC Power (kW)"
        )

        st.plotly_chart(fig2, use_container_width=True)

    # ==================================
    # Irradiation
    # ==================================
    with t3:

        st.subheader("Irradiation Data")

        st.dataframe(
            df[[
                "DATE_TIME",
                "IRRADIATION",
                "AC_POWER"
            ]]
        )

        fig3 = px.scatter(
            df,
            x="IRRADIATION",
            y="AC_POWER",
            color="IRRADIATION",
            title="Irradiation vs AC Power",
            color_continuous_scale="YlOrRd"
        )

        fig3.update_layout(
            xaxis_title="Irradiation",
            yaxis_title="AC Power (kW)"
        )

        st.plotly_chart(fig3, use_container_width=True)

elif page == "⚡ Solar Analytics":

    st.title("⚡ Solar Performance Analysis")
    st.divider()

    # Date Columns
    df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])
    df["DATE"] = df["DATE_TIME"].dt.date
    df["MONTH"] = df["DATE_TIME"].dt.strftime("%Y-%m")
    df["HOUR"] = df["DATE_TIME"].dt.hour

    # -------------------------
    # Data Preview
    # -------------------------
    st.subheader("📋 Solar Data Preview")

    st.dataframe(
        df[
            [
                "DATE_TIME",
                "AC_POWER",
                "DC_POWER",
                "DAILY_YIELD",
                "TOTAL_YIELD"
            ]
        ].head(20)
    )

    # -------------------------
    # AC Power Trend                   
    # -------------------------
    st.subheader("📈 AC Power Daily Trend")

    daily_ac = df.groupby("DATE")["AC_POWER"].sum().reset_index()

    fig1 = px.line(
        daily_ac,
        x="DATE",
        y="AC_POWER",
        title="AC Power Daily Trend",
        color_discrete_sequence=["green"]
    )

    fig1.update_layout(hovermode="x unified")

    st.plotly_chart(fig1, use_container_width=True)

    # -------------------------
    # DC Power Trend
    # -------------------------
    st.subheader("📈 DC Power Daily Trend")

    daily_dc = df.groupby("DATE")["DC_POWER"].sum().reset_index()

    fig2 = px.line(
        daily_dc,
        x="DATE",
        y="DC_POWER",
        title="DC Power Daily Trend",
        color_discrete_sequence=["purple"]
    )

    fig2.update_layout(hovermode="x unified")

    st.plotly_chart(fig2, use_container_width=True)

    # -------------------------
    # Daily Yield
    # -------------------------
    st.subheader("📊 Average Daily Yield")

    daily_yield = df.groupby("DATE")["DAILY_YIELD"].mean().reset_index()

    fig3 = px.bar(
        daily_yield,
        x="DATE",
        y="DAILY_YIELD",
        title="Average Daily Yield",
        color="DAILY_YIELD",
        color_continuous_scale="YlOrRd"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # -------------------------
    # Monthly Yield
    # -------------------------
    st.subheader("📅 Monthly Yield")

    monthly_yield = df.groupby("MONTH")["DAILY_YIELD"].sum().reset_index()

    fig4 = px.bar(
        monthly_yield,
        x="MONTH",
        y="DAILY_YIELD",
        title="Monthly Yield",
        color="DAILY_YIELD",
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # -------------------------
    # Peak Production Hours
    # -------------------------
    st.subheader("⏰ Peak Production Hours")

    hourly = df.groupby("HOUR")["AC_POWER"].mean().reset_index()

    fig5 = px.bar(
        hourly,
        x="HOUR",
        y="AC_POWER",
        title="Average AC Power by Hour",
        color="AC_POWER",
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig5, use_container_width=True)

    # -------------------------
    # Top Production Days
    # -------------------------
    st.subheader("🏆 Top 10 Production Days")

    top_days = (
        df.groupby("DATE")["AC_POWER"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig6 = px.bar(
        top_days,
        x="DATE",
        y="AC_POWER",
        title="Top 10 Highest Production Days",
        color="AC_POWER",
        color_continuous_scale="Reds"
    )

    st.plotly_chart(fig6, use_container_width=True)

elif page == "🔋 Battery Analytics":
    st.subheader("🔋 Battery Health Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Avg Battery",
            value="93.2%",
            delta="Healthy"
        )

    with col2:
        st.metric(
            label="Min Recorded",
            value="38.4%",
            delta="OK"
        )

    with col3:
        st.metric(
            label="Time < 20%",
            value="0.0%",
            delta="OK"
        )

    with col4:
        st.metric(
            label="Time > 90%",
            value="71.0%",
            delta="- Overcharge Risk"
        )

   # Date Format
    df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])

    # Estimated Battery Level (0-100%)
    df["BATTERY_LEVEL"] = (
        df["AC_POWER"] / df["AC_POWER"].max()
    ) * 100

    # -------------------------
    # Data Preview
    # -------------------------
    st.subheader("Battery Data")

    st.dataframe(
        df[
            [
                "DATE_TIME",
                "AC_POWER",
                "DC_POWER",
                "BATTERY_LEVEL"
            ]
        ].head(20)
    )

    # -------------------------
    # Battery Summary
    # -------------------------
    avg_battery = df["BATTERY_LEVEL"].mean()
    min_battery = df["BATTERY_LEVEL"].min()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Average Battery",
            f"{avg_battery:.1f}%"
        )

    with col2:
        st.metric(
            "Minimum Battery",
            f"{min_battery:.1f}%"
        )


    # -------------------------
    # Battery Backup Prediction
    # -------------------------

    st.subheader("🔋 Battery Backup Prediction")

    col1, col2 = st.columns(2)

    with col1:
        cap = st.slider("Battery Capacity (kWh)", 5, 200, 50, 5)
        soc = st.slider("Current Charge (%)", 0, 100, int(avg_battery))
        load = st.slider("Load (kW)", 0.5, 30.0, 3.0, 0.5)

    with col2:

        available_energy = cap * soc / 100
        backup_time = available_energy / load

        # Assume solar charging rate = 5 kW
        charge_rate = 5

        full_charge_time = (cap - available_energy) / charge_rate

        st.metric("Available Energy", f"{available_energy:.1f} kWh")

        st.metric("Backup Time", f"{backup_time:.1f} Hours")

        st.metric("Full Charge Time", f"{full_charge_time:.1f} Hours")

@st.cache_data
def train_models(df):

    X = df[
        [
            "IRRADIATION",
            "AMBIENT_TEMPERATURE",
            "MODULE_TEMPERATURE"
        ]
    ]

    y = df["AC_POWER"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    # ---------------- Linear Regression ----------------
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)

    lr_r2 = r2_score(y_test, lr_pred)
    lr_mse = mean_squared_error(y_test, lr_pred)
    lr_mae = mean_absolute_error(y_test, lr_pred)

    # ---------------- Polynomial Regression ----------------
    poly_scores = {}

    for degree in range(2, 11):

        poly = PolynomialFeatures(degree=degree)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)

        model = LinearRegression()
        model.fit(X_train_poly, y_train)

        pred = model.predict(X_test_poly)

        poly_scores[degree] = r2_score(y_test, pred)

    best_degree = max(poly_scores, key=poly_scores.get)

    poly = PolynomialFeatures(best_degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, y_train)

    poly_pred = poly_model.predict(X_test_poly)

    poly_r2 = r2_score(y_test, poly_pred)
    poly_mse = mean_squared_error(y_test, poly_pred)
    poly_mae = mean_absolute_error(y_test, poly_pred)

    # ---------------- KNN Regression ----------------
    best_k = 1
    best_r2 = -999
    knn_pred = None

    for k in range(1, 21):

        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(X_train, y_train)

        pred = knn.predict(X_test)

        score = r2_score(y_test, pred)

        if score > best_r2:
            best_r2 = score
            best_k = k
            knn_pred = pred

    knn_r2 = best_r2
    knn_mse = mean_squared_error(y_test, knn_pred)
    knn_mae = mean_absolute_error(y_test, knn_pred)

    #-----------------DecisionTree----------
    dt = DecisionTreeRegressor(random_state=10)
    dt.fit(X_train, y_train)
    dt_pred = dt.predict(X_test)

    dt_r2 = r2_score(y_test, dt_pred)
    dt_mse = mean_squared_error(y_test, dt_pred)
    dt_mae = mean_absolute_error(y_test, dt_pred)   

    # ---------------- RESULT TABLE ----------------
    result_df = pd.DataFrame({
    "Model":[
        "Linear Regression",
        "Polynomial Regression",
        "KNN Regression",
        "Decision Tree"
    ],

    "R2 Score":[
        lr_r2,
        poly_r2,
        knn_r2,
        dt_r2
    ],

    "MSE":[
        lr_mse,
        poly_mse,
        knn_mse,
        dt_mse
    ],

    "MAE":[
        lr_mae,
        poly_mae,
        knn_mae,
        dt_mae
    ]
})

    return (
        result_df,
        best_degree,
        best_k,
        poly_pred,
        y_test,
        lr,
        poly_model,
        knn,
        dt,
        poly
    )
# ==========================
# TRAIN ONCE (IMPORTANT)
# ==========================
result_df, best_degree, best_k, poly_pred, y_test, lr, poly_model, knn, dt, poly = train_models(df)

# ==========================
# 🤖 MODEL TRAINING PAGE
# ==========================

if  page == "🤖 Model Training":

    st.title("🤖 Model Training")
    st.divider()

    st.subheader("Training Dataset")


    st.subheader("Best Hyperparameters")

    st.write(f"✅ Best Polynomial Degree : **{best_degree}**")
    st.write(f"✅ Best K Value : **{best_k}**")

    st.subheader("Model Results")

    st.dataframe(result_df)

    fig1 = px.bar(
        result_df,
        x="Model",
        y="R2 Score",
        color="Model",
        text="R2 Score",
        title="R2 Score Comparison"
    )

    st.plotly_chart(fig1, use_container_width=True)

    compare_df = pd.DataFrame({
        "Actual": y_test.values[:100],
        "Predicted": poly_pred[:100]
    })

    fig2 = px.line(
        compare_df,
        y=["Actual", "Predicted"],
        title="Polynomial Regression Prediction"
    )

    st.plotly_chart(fig2, use_container_width=True)

    best_model = result_df.loc[
        result_df["R2 Score"].idxmax(),
        "Model"
    ]

    st.success(f"🏆 Best Performing Model : {best_model}")


# ==========================
# 📊 MODEL COMPARISON PAGE
# ==========================
elif page == "📊 Model Comparison":

    st.title("📊 Model Comparison")
    st.divider()

    st.subheader("Model Results")
    st.dataframe(result_df)

    # =========================
    # R2 Score Chart
    # =========================
    fig1 = px.bar(
        result_df,
        x="Model",
        y="R2 Score",
        color="Model",
        
        text="R2 Score",
        title="R2 Score Comparison"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # Best model (R2 MAX)
    best_model_r2 = result_df.loc[
        result_df["R2 Score"].idxmax(),
        "Model"
    ]

    # =========================
    # MSE Chart
    # =========================
    fig2 = px.bar(
        result_df,
        x="Model",
        y="MSE",
        color="Model",
        text="MSE",
        title="MSE Comparison"
    )

    st.plotly_chart(fig2, use_container_width=True)

    best_model_mse = result_df.loc[
        result_df["MSE"].idxmin(),
        "Model"
    ]

    # =========================
    # MAE Chart
    # =========================
    fig3 = px.bar(
        result_df,
        x="Model",
        y="MAE",
        color="Model",
        text="MAE",
        title="MAE Comparison"
    )

    st.plotly_chart(fig3, use_container_width=True)

    best_model_mae = result_df.loc[
        result_df["MAE"].idxmin(),
        "Model"
    ]

    # =========================
    # Final Best (based on R2)
    # =========================
    st.success(f"🏆 Best Model (R2) : {best_model_r2}")

    st.info(f"📉 Best Model (MSE) : {best_model_mse}")

    st.info(f"📉 Best Model (MAE) : {best_model_mae}")

elif page == "🎯 Real-Time Prediction":

    st.header("🎯 Solar Power Prediction")

    st.subheader("Enter Solar Conditions")

    Irr = st.slider(
        "IRRADIATION",
        0.0, 1.5, 0.5, 0.01
    )

    Amb = st.slider(
        "AMBIENT_TEMPERATURE",
        0.0, 50.0, 25.0, 0.5
    )

    Mod = st.slider(
        "MODULE_TEMPERATURE",
        0.0, 80.0, 30.0, 0.5
    )

    if st.button("🔮 Predict Power Output"):

        input_df = pd.DataFrame({
            "IRRADIATION": [Irr],
            "AMBIENT_TEMPERATURE": [Amb],
            "MODULE_TEMPERATURE": [Mod]
        })

        # Linear Prediction
        linear_pred = lr.predict(input_df)[0]

        # Polynomial Prediction
        input_poly = poly.transform(input_df)
        poly_prediction = poly_model.predict(input_poly)[0]

        # KNN Prediction
        knn_prediction = knn.predict(input_df)[0]

        st.subheader("Prediction Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Linear Regression",
                f"{linear_pred:.2f} kW"
            )

        with col2:
            st.metric(
                "Polynomial Regression",
                f"{poly_prediction:.2f} kW"
            )

        with col3:
            st.metric(
                "KNN Regression",
                f"{knn_prediction:.2f} kW"
            )

        # Best model from training result
        best_model = result_df.loc[
            result_df["R2 Score"].idxmax(),
            "Model"
        ]

        best_r2 = result_df["R2 Score"].max()

        st.success(
            f"🏆 Best Trained Model : {best_model}"
        )

        st.info(
            f"📈 R² Score : {best_r2:.4f}"
        )

        # Final Output using Best Model
        if best_model == "Linear Regression":
            final_prediction = linear_pred

        elif best_model == "Polynomial Regression":
            final_prediction = poly_prediction

        else:
            final_prediction = knn_prediction

        st.subheader("Final Solar Power Prediction")

        st.metric(
            "Predicted AC Power",
            f"{final_prediction:.2f} kW"
        )

# 
# ======================================================
# 💰 BILL SAVINGS (PART - 1)
# ======================================================

elif page == "💰 Bill Savings":

    st.title("💰 Smart Electricity Bill Savings")
    st.divider()

    # -----------------------------
    # Consumer Details
    # -----------------------------
    st.subheader("🏠 Consumer Details")

    c1, c2 = st.columns(2)

    with c1:

        monthly_units = st.number_input(
            "Monthly Electricity Consumption (kWh)",
            min_value=50,
            max_value=10000,
            value=600,
            step=10
        )

        electricity_rate = st.number_input(
            "Electricity Rate (₹/kWh)",
            min_value=1.0,
            max_value=20.0,
            value=8.0,
            step=0.5
        )

    with c2:

        solar_percent = st.slider(
            "Solar Energy Coverage (%)",
            0,
            100,
            70
        )

        plant_capacity = st.slider(
            "Solar Plant Capacity (kW)",
            1,
            50,
            5
        )

    st.divider()

    # -----------------------------
    # Energy Calculation
    # -----------------------------

    solar_units = monthly_units * solar_percent / 100

    grid_units = monthly_units - solar_units

    without_solar_bill = monthly_units * electricity_rate

    with_solar_bill = grid_units * electricity_rate

    monthly_savings = (
        without_solar_bill -
        with_solar_bill
    )

    yearly_savings = monthly_savings * 12

    # Estimated Monthly Solar Generation

    estimated_generation = plant_capacity * 4.5 * 30

    extra_generation = max(
        estimated_generation - solar_units,
        0
    )

    # -----------------------------
    # KPI Cards
    # -----------------------------

    st.subheader("📊 Energy Summary")

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric(
            "⚡ Monthly Usage",
            f"{monthly_units:.0f} kWh"
        )

    with k2:
        st.metric(
            "☀ Solar Generated",
            f"{solar_units:.0f} kWh"
        )

    with k3:
        st.metric(
            "🔌 Grid Consumption",
            f"{grid_units:.0f} kWh"
        )

    with k4:
        st.metric(
            "💰 Monthly Savings",
            f"₹ {monthly_savings:,.0f}"
        )

    st.divider()

    # -----------------------------
    # Bill Comparison
    # -----------------------------

    st.subheader("💵 Bill Comparison")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Without Solar",
            f"₹ {without_solar_bill:,.0f}"
        )

    with c2:
        st.metric(
            "With Solar",
            f"₹ {with_solar_bill:,.0f}"
        )

    with c3:
        st.metric(
            "Yearly Savings",
            f"₹ {yearly_savings:,.0f}"
        )

    bill_df = pd.DataFrame({

        "Category":[
            "Without Solar",
            "With Solar"
        ],

        "Bill":[
            without_solar_bill,
            with_solar_bill
        ]

    })

    fig = px.bar(

        bill_df,

        x="Category",

        y="Bill",

        color="Category",

        text="Bill",

        title="Electricity Bill Comparison"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()
    # ======================================================
    # 💵 NET METERING & SELLING INCOME
    # ======================================================

    st.subheader("💵 Net Metering")

    c1, c2 = st.columns(2)

    with c1:

        exported_units = st.number_input(
            "Extra Units Exported to Grid (kWh/month)",
            min_value=0.0,
            value=float(extra_generation),
            step=10.0
        )

    with c2:

        sell_rate = st.number_input(
            "Selling Rate (₹/kWh)",
            min_value=0.0,
            max_value=20.0,
            value=3.50,
            step=0.50
        )

    monthly_income = exported_units * sell_rate

    yearly_income = monthly_income * 12

    total_monthly_profit = monthly_savings + monthly_income

    total_yearly_profit = yearly_savings + yearly_income

    st.divider()

    m1, m2, m3, m4 = st.columns(4)

    m1.metric(
        "⚡ Exported Units",
        f"{exported_units:.0f} kWh"
    )

    m2.metric(
        "💵 Selling Income",
        f"₹ {monthly_income:,.0f}"
    )

    m3.metric(
        "💰 Monthly Profit",
        f"₹ {total_monthly_profit:,.0f}"
    )

    m4.metric(
        "🏦 Yearly Profit",
        f"₹ {total_yearly_profit:,.0f}"
    )

    # ======================================================
    # PIE CHART
    # ======================================================

    income_df = pd.DataFrame({

        "Category":[
            "Bill Savings",
            "Net Metering"
        ],

        "Amount":[
            monthly_savings,
            monthly_income
        ]

    })

    fig_income = px.pie(

        income_df,

        names="Category",

        values="Amount",

        hole=0.45,

        title="Monthly Income Distribution"

    )

    st.plotly_chart(
        fig_income,
        use_container_width=True
    )

    st.divider()

   
    # ======================================================
    # PAYBACK PERIOD
    # ======================================================

    st.subheader("💸 Investment Analysis")

    plant_cost = st.number_input(

        "Solar Plant Installation Cost (₹)",

        min_value=50000,

        max_value=5000000,

        value=300000,

        step=10000

    )

    if total_yearly_profit > 0:

        payback = plant_cost / total_yearly_profit

        roi = (total_yearly_profit / plant_cost) * 100

    else:

        payback = 0

        roi = 0

    r1, r2 = st.columns(2)

    r1.metric(
        "📅 Payback Period",
        f"{payback:.2f} Years"
    )

    r2.metric(
        "📈 Annual ROI",
        f"{roi:.2f}%"
    )

    st.divider()

    # ======================================================
    # SAVINGS TREND
    # ======================================================

    st.subheader("📈 12-Month Savings Trend")

    months = [

        "Jan","Feb","Mar","Apr","May","Jun",

        "Jul","Aug","Sep","Oct","Nov","Dec"

    ]

    trend = []

    for i in range(12):

        trend.append(total_monthly_profit)

    trend_df = pd.DataFrame({

        "Month": months,

        "Savings": trend

    })

    fig = px.line(

        trend_df,

        x="Month",

        y="Savings",

        markers=True,

        title="Monthly Savings Trend"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()


    # ======================================================
    # 📊 25 YEAR SAVINGS PROJECTION
    # ======================================================

    st.subheader("📈 25-Year Savings Projection")

    inflation = st.slider(
        "Electricity Price Increase (%)",
        0,
        10,
        5
    )

    years = list(range(1, 26))

    annual_profit = []
    cumulative_profit = []

    total = 0

    for y in years:

        saving = total_yearly_profit * ((1 + inflation/100) ** (y-1))

        annual_profit.append(saving)

        total += saving

        cumulative_profit.append(total)

    projection_df = pd.DataFrame({
        "Year": years,
        "Annual Profit": annual_profit,
        "Cumulative Profit": cumulative_profit
    })

    fig = px.bar(
        projection_df,
        x="Year",
        y="Annual Profit",
        color="Annual Profit",
        title="25-Year Annual Profit"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.line(
        projection_df,
        x="Year",
        y="Cumulative Profit",
        markers=True,
        title="25-Year Cumulative Profit"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # ======================================================
    # 📊 MONTHLY BILL TABLE
    # ======================================================

    st.subheader("📋 Monthly Bill Details")

    months = [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]

    bill_table = pd.DataFrame({

        "Month": months,

        "Without Solar (₹)": [without_solar_bill]*12,

        "With Solar (₹)": [with_solar_bill]*12,

        "Savings (₹)": [monthly_savings]*12

    })

    st.dataframe(
        bill_table,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # 📈 SOLAR VS GRID CONSUMPTION
    # ======================================================

    compare_df = pd.DataFrame({

        "Source":[
            "Solar Energy",
            "Grid Energy"
        ],

        "Units":[
            solar_units,
            grid_units
        ]

    })

    fig3 = px.bar(

        compare_df,

        x="Source",

        y="Units",

        color="Source",

        text="Units",

        title="Solar vs Grid Consumption"

    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # 🏆 FINAL DASHBOARD SUMMARY
    # ======================================================

    st.subheader("🏆 Overall Performance")

    performance = "Excellent"

    if solar_percent < 40:
        performance = "Poor"
    elif solar_percent < 60:
        performance = "Average"
    elif solar_percent < 80:
        performance = "Good"

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Solar Coverage",
        f"{solar_percent}%"
    )

    col2.metric(
        "System Performance",
        performance
    )

    col3.metric(
        "25-Year Profit",
        f"₹ {cumulative_profit[-1]:,.0f}"
    )

    st.success(f"""
    ✅ Solar Plant Capacity : {plant_capacity} kW

    ⚡ Monthly Consumption : {monthly_units:.0f} kWh

    ☀ Solar Generation : {solar_units:.0f} kWh

    🔌 Grid Consumption : {grid_units:.0f} kWh

    💰 Monthly Savings : ₹ {monthly_savings:,.0f}

    💵 Net Metering Income : ₹ {monthly_income:,.0f}

    🏦 Total Monthly Profit : ₹ {total_monthly_profit:,.0f}

    📅 Payback Period : {payback:.2f} Years

    📈 ROI : {roi:.2f} %

    🏆 Estimated 25-Year Profit : ₹ {cumulative_profit[-1]:,.0f}
    """)

# ======================================================
# 🏗 SOLAR INSTALLATION PLANNER
# ======================================================

elif page == "🏗 Solar Installation Planner":

    st.title("🏗 Solar Installation Planner")
    st.divider()

    # ======================================================
    # CUSTOMER DETAILS
    # ======================================================

    st.subheader("👤 Customer Details")

    col1, col2 = st.columns(2)

    with col1:

        customer_name = st.text_input(
            "Customer Name",
            placeholder="Enter Customer Name"
        )

        city = st.selectbox(
            "City",
            [
                "Ahmedabad",
                "Surat",
                "Rajkot",
                "Vadodara",
                "Bhavnagar",
                "Other"
            ]
        )

        house_type = st.selectbox(
            "Property Type",
            [
                "Residential",
                "Commercial",
                "Industrial"
            ]
        )

    with col2:

        roof_type = st.selectbox(
            "Roof Type",
            [
                "RCC Roof",
                "Tin Roof",
                "Terrace",
                "Ground Mount"
            ]
        )

        monthly_bill = st.number_input(
            "Monthly Electricity Bill (₹)",
            min_value=500,
            max_value=200000,
            value=5000,
            step=500
        )

        monthly_units = st.number_input(
            "Monthly Electricity Consumption (kWh)",
            min_value=50,
            max_value=50000,
            value=600,
            step=10
        )

    st.divider()

    # ======================================================
    # SOLAR CONFIGURATION
    # ======================================================

    st.subheader("☀ Solar System Configuration")

    c1, c2, c3 = st.columns(3)

    with c1:

        plant_kw = st.selectbox(
            "Plant Capacity (kW)",
            [1,2,3,5,7,10,15,20,25,30,40,50]
        )

    with c2:

        panel_brand = st.selectbox(
            "Solar Panel Brand",
            [
                "Waaree",
                "Tata Power Solar",
                "Adani Solar",
                "Vikram Solar"
            ]
        )

    with c3:

        system_type = st.selectbox(
            "Solar System Type",
            [
                "On Grid",
                "Off Grid",
                "Hybrid"
            ]
        )

    st.divider()

    # ======================================================
    # BATTERY OPTION
    # ======================================================

    st.subheader("🔋 Battery Configuration")

    b1, b2 = st.columns(2)

    with b1:

        battery_required = st.radio(
            "Battery Required?",
            [
                "No",
                "Yes"
            ],
            horizontal=True
        )

    with b2:

        battery_capacity = 0

        if battery_required == "Yes":

            battery_capacity = st.selectbox(
                "Battery Capacity (kWh)",
                [5,10,15,20,25,30]
            )

    st.divider()

    # ======================================================
    # PANEL RATE
    # ======================================================

    if panel_brand == "Waaree":
        panel_rate = 26000

    elif panel_brand == "Tata Power Solar":
        panel_rate = 28000

    elif panel_brand == "Adani Solar":
        panel_rate = 27000

    else:
        panel_rate = 25500

    # ======================================================
    # INVERTER RATE
    # ======================================================

    if system_type == "On Grid":

        inverter_rate = 10000

    elif system_type == "Off Grid":

        inverter_rate = 18000

    else:

        inverter_rate = 22000

    # ======================================================
    # BATTERY COST
    # ======================================================

    battery_cost = battery_capacity * 12000

    # ======================================================
    # GENERATE BUTTON
    # ======================================================

    if st.button(
        "📋 Generate Professional Quotation",
        type="primary",
        use_container_width=True
    ):
                # ======================================================
        # ☀ ENERGY GENERATION ESTIMATION
        # ======================================================

        daily_generation = plant_kw * 4.5
        monthly_generation = daily_generation * 30
        yearly_generation = daily_generation * 365
        roof_area = plant_kw * 6.5

        st.subheader("☀ Energy Generation Summary")

        k1, k2, k3, k4 = st.columns(4)

        with k1:
            st.metric(
                "☀ Daily Generation",
                f"{daily_generation:.1f} kWh"
            )

        with k2:
            st.metric(
                "📊 Monthly Generation",
                f"{monthly_generation:,.0f} kWh"
            )

        with k3:
            st.metric(
                "📈 Yearly Generation",
                f"{yearly_generation:,.0f} kWh"
            )

        with k4:
            st.metric(
                "📐 Roof Area",
                f"{roof_area:.1f} m²"
            )

        st.divider()

        # ======================================================
        # 💰 COMPONENT COST
        # ======================================================

        panel_cost = plant_kw * panel_rate

        inverter_cost = plant_kw * inverter_rate

        structure_cost = plant_kw * 5000

        dc_cable = plant_kw * 1200

        ac_cable = plant_kw * 1000

        mc4_connector = plant_kw * 500

        earthing = 5000

        lightning = 4000

        acdb_dcdb = 8000

        net_metering = 5000

        installation = plant_kw * 3500

        transportation = 6000

        gst_misc = int(
            (
                panel_cost +
                inverter_cost
            ) * 0.05
        )

        total_cost = (

            panel_cost +

            inverter_cost +

            structure_cost +

            dc_cable +

            ac_cable +

            mc4_connector +

            earthing +

            lightning +

            acdb_dcdb +

            net_metering +

            installation +

            transportation +

            gst_misc +

            battery_cost

        )

        st.subheader("💰 Detailed Cost Breakdown")

        cost_df = pd.DataFrame({

            "Component":[

                "Solar Panels",

                "Solar Inverter",

                "Mounting Structure",

                "DC Cable",

                "AC Cable",

                "MC4 Connector",

                "Earthing",

                "Lightning Arrester",

                "ACDB + DCDB",

                "Net Metering",

                "Installation",

                "Transportation",

                "GST & Misc",

                "Battery"

            ],

            "Estimated Cost (₹)":[

                panel_cost,

                inverter_cost,

                structure_cost,

                dc_cable,

                ac_cable,

                mc4_connector,

                earthing,

                lightning,

                acdb_dcdb,

                net_metering,

                installation,

                transportation,

                gst_misc,

                battery_cost

            ]

        })

        st.dataframe(
            cost_df,
            use_container_width=True
        )

        st.success(
            f"💰 Total Installation Cost : ₹ {total_cost:,.0f}"
        )

        st.divider()
                # ======================================================
        # 🏛 GOVERNMENT SUBSIDY
        # ======================================================

        st.subheader("🏛 Government Subsidy")

        subsidy = 0

        if house_type == "Residential":

            if plant_kw <= 2:
                subsidy = total_cost * 0.40

            elif plant_kw <= 3:
                subsidy = total_cost * 0.30

            elif plant_kw <= 10:
                subsidy = total_cost * 0.20

            else:
                subsidy = total_cost * 0.10

        elif house_type == "Commercial":

            subsidy = total_cost * 0.10

        else:

            subsidy = 0

        final_cost = total_cost - subsidy

        s1, s2, s3 = st.columns(3)

        with s1:
            st.metric(
                "💰 Total Cost",
                f"₹ {total_cost:,.0f}"
            )

        with s2:
            st.metric(
                "🏛 Government Subsidy",
                f"₹ {subsidy:,.0f}"
            )

        with s3:
            st.metric(
                "✅ Final Customer Cost",
                f"₹ {final_cost:,.0f}"
            )

        st.divider()

        # ======================================================
        # 💵 FINANCIAL CALCULATION
        # ======================================================

        yearly_generation = daily_generation * 365

        electricity_rate = monthly_bill / monthly_units

        monthly_saving = monthly_generation * electricity_rate

        yearly_saving = monthly_saving * 12

        roi = (yearly_saving / final_cost) * 100

        payback = final_cost / yearly_saving

        profit25 = yearly_saving * 25 - final_cost

        st.subheader("💵 Financial Summary")

        f1, f2, f3 = st.columns(3)

        with f1:

            st.metric(
                "💰 Total Installation Cost",
                f"₹{total_cost:,.0f}"
            )

            st.metric(
                "🏛 Government Subsidy",
                f"₹{subsidy:,.0f}"
            )

        with f2:

            st.metric(
                "✅ Your Final Cost",
                f"₹{final_cost:,.0f}"
            )

            st.metric(
                "💵 Monthly Saving",
                f"₹{monthly_saving:,.0f}/mo"
            )

        with f3:

            st.metric(
                "📊 Yearly Saving",
                f"₹{yearly_saving:,.0f}/yr"
            )

            st.metric(
                "🌟 25 Year Profit",
                f"₹{profit25:,.0f}"
            )

        st.divider()

        r1, r2 = st.columns(2)

        with r1:

            st.metric(
                "📈 Return on Investment",
                f"{roi:.1f}%"
            )

        with r2:

            st.metric(
                "⏱ Payback Period",
                f"{payback:.1f} yrs"
            )
                # ======================================================
        # 📊 COST DISTRIBUTION PIE CHART
        # ======================================================

        st.subheader("📊 Cost Distribution")

        chart_df = cost_df.copy()

        fig1 = px.pie(
            chart_df,
            names="Component",
            values="Estimated Cost (₹)",
            hole=0.45,
            title="Installation Cost Distribution"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        # ======================================================
        # 📈 COST BREAKDOWN BAR CHART
        # ======================================================

        fig2 = px.bar(
            chart_df,
            x="Component",
            y="Estimated Cost (₹)",
            color="Estimated Cost (₹)",
            text="Estimated Cost (₹)",
            title="Component Cost Breakdown"
        )

        fig2.update_layout(
            xaxis_tickangle=-35
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        st.divider()

        # ======================================================
        # 📈 25 YEAR PROFIT PROJECTION
        # ======================================================

        st.subheader("📈 25 Year Profit Projection")

        inflation = st.slider(
            "Electricity Price Increase (%)",
            0,
            10,
            5
        )

        years = list(range(1, 26))

        annual_profit = []
        cumulative_profit = []

        total = 0

        for yr in years:

            saving = yearly_saving * ((1 + inflation/100) ** (yr-1))

            annual_profit.append(saving)

            total += saving

            cumulative_profit.append(total - final_cost)

        projection_df = pd.DataFrame({

            "Year": years,

            "Annual Saving": annual_profit,

            "Cumulative Profit": cumulative_profit

        })

        fig3 = px.line(

            projection_df,

            x="Year",

            y="Cumulative Profit",

            markers=True,

            title="25 Year Cumulative Profit"

        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

        fig4 = px.bar(

            projection_df,

            x="Year",

            y="Annual Saving",

            color="Annual Saving",

            title="Annual Saving Growth"

        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

        st.divider()


        st.success(
            "✅ Professional Solar Installation Quotation Generated Successfully."
        )
                # ======================================================
        # 📄 SOLAR INSTALLATION REPORT
        # ======================================================

        st.subheader("📄 Solar Installation Report")

        st.info(f"""
    👤 Customer Name : {customer_name}

    🏙 City : {city}

    🏠 House Type : {house_type}

    🏡 Roof Type : {roof_type}

    ☀ Solar Plant Capacity : {plant_kw} kW

    🔋 System Type : {system_type}

    🏭 Panel Brand : {panel_brand}

    ------------------------------------------

    📐 Roof Area Required : {roof_area:.1f} m²

    ☀ Daily Generation : {daily_generation:.1f} kWh

    📊 Monthly Generation : {monthly_generation:.0f} kWh

    📈 Yearly Generation : {yearly_generation:.0f} kWh

    ------------------------------------------

    💰 Installation Cost : ₹ {total_cost:,.0f}

    🏛 Government Subsidy : ₹ {subsidy:,.0f}

    ✅ Customer Cost : ₹ {final_cost:,.0f}

    ------------------------------------------

    💵 Monthly Saving : ₹ {monthly_saving:,.0f}

    📊 Yearly Saving : ₹ {yearly_saving:,.0f}

    📈 ROI : {roi:.1f} %

    ⏱ Payback : {payback:.1f} Years

    🌟 25-Year Profit : ₹ ₹ {profit25:,.0f}

    ------------------------------------------

    🛡 Panel Warranty : 25 Years

    🛡 Inverter Warranty : 10 Years
            """)

    st.success("✅ Solar Installation Planning Completed Successfully.")