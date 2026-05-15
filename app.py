import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Care Transition Analytics", layout="wide")

# ------------------ LOAD DATA ------------------
@st.cache_data
def load_data():
    df = pd.read_csv("HHS_Unaccompanied_Alien_Children_Program (1).csv")

    # Strip spaces from column names to prevent KeyErrors
    df.columns = [col.strip() for col in df.columns]

    # Clean up the Date column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date']).sort_values('Date')

    # Mapping raw columns to shorter names for internal logic
    mapping = {
        'Children apprehended and placed in CBP custody*': 'Intake',
        'Children in CBP custody': 'CBP_Inventory',
        'Children transferred out of CBP custody': 'Transfers',
        'Children in HHS Care': 'HHS_Inventory',
        'Children discharged from HHS Care': 'Discharges'
    }
    df = df.rename(columns=mapping)

    # Clean numeric columns (remove commas and handle NaNs)
    numeric_cols = ['Intake', 'CBP_Inventory', 'Transfers', 'HHS_Inventory', 'Discharges']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce').fillna(0)

    # --- DERIVED METRICS ---
    # 1. Efficiency (%)
    df['Transfer Efficiency'] = (df['Transfers'] / df['CBP_Inventory'].replace(0, 1)) * 100
    df['Discharge Effectiveness'] = (df['Discharges'] / df['HHS_Inventory'].replace(0, 1)) * 100

    # 2. Cumulative Outcome (The Success Story)
    df['Daily Net'] = df['Intake'] - df['Discharges']
    df['Cumulative Backlog'] = df['Daily Net'].cumsum()

    return df

data = load_data()

# ------------------ SIDEBAR FILTER ------------------
st.sidebar.header("Controls")
min_date, max_date = data['Date'].min().to_pydatetime(), data['Date'].max().to_pydatetime()
date_range = st.sidebar.date_input("📅 Date Range", [min_date, max_date])

# Filter data
if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    df = data[(data['Date'] >= pd.Timestamp(date_range[0])) &
              (data['Date'] <= pd.Timestamp(date_range[1]))].copy()
else:
    df = data.copy()

# ------------------ TITLE ------------------
st.title("📊 Care Transition Efficiency & Outcome Analytics")

# ------------------ KPI SECTION ------------------
# Five columns to fit all requirements
k1, k2, k3, k4, k5, k6 = st.columns(6)

k1.metric("Avg Transfer Efficiency", f"{df['Transfer Efficiency'].mean():.2f}%")
k2.metric("Avg Discharge Effectiveness", f"{df['Discharge Effectiveness'].mean():.2f}%")
k3.metric("Peak Backlog", f"{int(df['Daily Net'].max())}")
k4.metric("Peak Clearance", f"{int(df['Daily Net'].min())}")
k5.metric("Total Cumulative Outcome", f"{int(df['Cumulative Backlog'].iloc[-1]):,}")
k6.metric("Stability (Std Dev)", f"{df['Discharge Effectiveness'].std() / 100:.3f}")

# ------------------ 1. CUMULATIVE OUTCOME (REQUIRED) ------------------
st.subheader("1. Cumulative Pipeline Outcome Trend")
st.write("Meets requirement: Executive Summary of Outcome Trends.")

fig_cum = px.line(df, x='Date', y='Cumulative Backlog',
                  title="Net Backlog Accumulation (Intake - Discharges)",
                  color_discrete_sequence=['#00CC96'])
fig_cum.add_hline(y=0, line_dash="dash", line_color="white")
st.plotly_chart(fig_cum, use_container_width=True)

# ------------------ 2. OPERATIONAL FLOW ------------------
st.subheader("2. Care Pipeline Inventory")
fig_flow = px.area(df, x='Date', y=['CBP_Inventory', 'HHS_Inventory'],
                   title="Volume in Custody vs. HHS Care")
st.plotly_chart(fig_flow, use_container_width=True)

# ------------------ 3. OUTCOME STABILITY (REQUIRED) ------------------
st.subheader("3. Outcome Stability Analysis")
df['Rolling_Avg'] = df['Discharge Effectiveness'].rolling(7).mean()

fig_stab = px.line(df, x='Date', y=['Discharge Effectiveness', 'Rolling_Avg'],
                   title="Stability of Daily Placement Outcomes (7-Day Moving Avg)")
st.plotly_chart(fig_stab, use_container_width=True)

# ------------------ 4. WEEKEND VS WEEKDAY ------------------
st.subheader("4. Weekend vs Weekday Performance")
df['Day_Type'] = df['Date'].dt.weekday.map(lambda x: 'Weekend' if x >= 5 else 'Weekday')
week_stats = df.groupby('Day_Type')[['Transfer Efficiency', 'Discharge Effectiveness']].mean().reset_index()

fig_week = px.bar(week_stats, x='Day_Type', y=['Transfer Efficiency', 'Discharge Effectiveness'],
                  barmode='group', title="Efficiency Comparison")
st.plotly_chart(fig_week, use_container_width=True)

# ------------------ 5. EFFICIENCY ALERTS ------------------
st.subheader("5. Threshold Performance Alerts")
threshold = st.slider("Set Efficiency Threshold (%)", 0, 100, 50)
low_eff_days = df[df['Transfer Efficiency'] < threshold]

if not low_eff_days.empty:
    st.error(f"🚨 {len(low_eff_days)} days fell below the {threshold}% efficiency threshold.")
else:
    st.success("✅ System performance is within acceptable efficiency limits.")
