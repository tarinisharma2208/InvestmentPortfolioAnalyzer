import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Investment Portfolio Analyzer")

st.title("📈 Investment Portfolio Analyzer")

st.write("Upload your portfolio CSV file.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    required_cols = ["Stock", "Quantity", "Buy_Price", "Current_Price"]
    
    if not all(col in df.columns for col in required_cols):
        st.error("CSV must contain: Stock, Quantity, Buy_Price, Current_Price")
    else:
        st.subheader("📋 Portfolio Data")
        st.write(df)

        # Calculate investment values
        df["Invested_Amount"] = df["Quantity"] * df["Buy_Price"]
        df["Current_Value"] = df["Quantity"] * df["Current_Price"]
        df["Profit_Loss"] = df["Current_Value"] - df["Invested_Amount"]
        df["Return_%"] = (df["Profit_Loss"] / df["Invested_Amount"]) * 100

        total_invested = df["Invested_Amount"].sum()
        total_current = df["Current_Value"].sum()
        total_profit = df["Profit_Loss"].sum()
        total_return = (total_profit / total_invested) * 100

        st.subheader("💰 Portfolio Summary")
        st.write(f"Total Invested: ₹ {total_invested:.2f}")
        st.write(f"Current Value: ₹ {total_current:.2f}")
        st.write(f"Total Profit/Loss: ₹ {total_profit:.2f}")
        st.write(f"Overall Return: {total_return:.2f}%")

        # Pie Chart (Allocation)
        st.subheader("🥧 Portfolio Allocation")
        fig1, ax1 = plt.subplots()
        ax1.pie(df["Current_Value"], labels=df["Stock"], autopct="%1.1f%%")
        st.pyplot(fig1)

        # Bar Chart (Returns per stock)
        st.subheader("📊 Stock-wise Return %")
        fig2, ax2 = plt.subplots()
        ax2.bar(df["Stock"], df["Return_%"])
        ax2.set_ylabel("Return %")
        ax2.set_xlabel("Stock")
        st.pyplot(fig2)

else:
    st.info("Please upload a portfolio CSV file.")
