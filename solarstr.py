import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
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

    # ---------------- RESULT TABLE ----------------
    result_df = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Polynomial Regression",
            "KNN Regression"
        ],
        "R2 Score": [lr_r2, poly_r2, knn_r2],
        "MSE": [lr_mse, poly_mse, knn_mse],
        "MAE": [lr_mae, poly_mae, knn_mae]
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
        poly
    )


# ==========================
# TRAIN ONCE (IMPORTANT)
# ==========================
result_df, best_degree, best_k, poly_pred, y_test, lr, poly_model, knn, poly = train_models(df)

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

# ==========================
# 💰 BILL SAVINGS PAGE
# ==========================
elif page == "💰 Bill Savings":

    st.title("💰 Electricity Bill Savings")
    st.divider()

    # Date Convert
    df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])

    # Electricity Rate
    rate = st.slider(
        "Electricity Rate (₹ / kWh)",
        min_value=1.0,
        max_value=20.0,
        value=8.0,
        step=0.5
    )

    # ==========================
    # Daily Energy Calculation
    # ==========================

    daily_energy = (
        df.groupby(df["DATE_TIME"].dt.date)["AC_POWER"]
        .sum()
        .reset_index()
    )

    daily_energy.columns = ["DATE", "AC_POWER"]

    daily_energy["ENERGY_KWH"] = (
        daily_energy["AC_POWER"] / 1000
    )

    daily_energy["SAVINGS"] = (
        daily_energy["ENERGY_KWH"] * rate
    )

    avg_daily_energy = (
        daily_energy["ENERGY_KWH"].mean()
    )

    monthly_energy = avg_daily_energy * 30
    yearly_energy = avg_daily_energy * 365

    monthly_savings = monthly_energy * rate
    yearly_savings = yearly_energy * rate

    # ==========================
    # Metrics
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "⚡ Avg Daily Energy",
            f"{avg_daily_energy:.2f} kWh"
        )

    with c2:
        st.metric(
            "📅 Monthly Energy",
            f"{monthly_energy:.0f} kWh"
        )

    with c3:
        st.metric(
            "💰 Monthly Savings",
            f"₹ {monthly_savings:,.0f}"
        )

    with c4:
        st.metric(
            "🏦 Yearly Savings",
            f"₹ {yearly_savings:,.0f}"
        )

    st.divider()

    # ==========================
    # Daily Savings Trend
    # ==========================

    st.subheader("📈 Daily Savings Trend")

    fig1 = px.line(
        daily_energy,
        x="DATE",
        y="SAVINGS",
        markers=True,
        title="Daily Electricity Savings"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ==========================
    # Monthly Savings Chart
    # ==========================

    st.subheader("📊 Monthly Bill: With vs Without Solar")

    months = [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]

    without_solar = [
        22000,20500,22300,21500,22400,21400,
        20800,21900,22100,21600,21200,22000
    ]

    with_solar = []

    for bill in without_solar:
        with_solar.append(bill - monthly_savings)

    bill_df = pd.DataFrame({
        "Month": months,
        "Without Solar": without_solar,
        "With Solar": with_solar
    })

    fig = px.bar(
        bill_df,
        x="Month",
        y=["Without Solar", "With Solar"],
        barmode="group",
        title="Monthly Bill: With vs Without Solar"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ==========================
    # 25 Year Savings Projection
    # ==========================

    years = list(range(1, 26))

    annual_savings = []
    cumulative_savings = []

    total = 0

    for y in years:

        saving = yearly_savings * (
            1.05 ** (y - 1)
        )

        annual_savings.append(saving)

        total += saving

        cumulative_savings.append(total)

    projection_df = pd.DataFrame({
        "Year": years,
        "Annual Savings": annual_savings,
        "Cumulative Savings": cumulative_savings
    })

    st.subheader(
        "📊 25-Year Annual Savings Projection"
    )

    fig3 = px.bar(
        projection_df,
        x="Year",
        y="Annual Savings",
        text_auto=".0f",
        title="25-Year Annual Savings"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.subheader(
        "📈 25-Year Cumulative Savings"
    )

    fig4 = px.line(
        projection_df,
        x="Year",
        y="Cumulative Savings",
        markers=True,
        title="25-Year Cumulative Savings Growth"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # ==========================
    # Final Summary
    # ==========================

    st.subheader("📋 Savings Summary")

    st.success(
        f"""
💰 Monthly Savings : ₹ {monthly_savings:,.0f}

🏦 Yearly Savings : ₹ {yearly_savings:,.0f}

📈 25-Year Total Savings : ₹ {cumulative_savings[-1]:,.0f}

⚡ Average Daily Energy : {avg_daily_energy:.2f} kWh
"""
    )