import pandas as pd
import streamlit as st
import datetime
import yfinance as yf

microsoft = yf.Ticker("MSFT")
nvidia = yf.Ticker("NVDA")
apple = yf.Ticker("AAPL")
google = yf.Ticker("GOOGL")
tesla = yf.Ticker("TSLA")

companies = {
    "Microsoft": microsoft,
    "NVIDIA": nvidia,
    "Apple": apple,
    "Google": google,
    "Tesla": tesla
    }
st.set_page_config(page_title="Finance", page_icon="📊")

st.markdown("# Yahoo! Finance Ticker Dashboard")
st.sidebar.header("Access Financial Data Below:")


def company(): #NEW
    st.sidebar.subheader("Choose Company")
    company_select = st.sidebar.radio(
    "Select 1",
    companies.keys()
    )
    return company_select


chosen_company = company()


def start_date_input(): #NEW
    st.sidebar.subheader("Input start and end dates")
    start_date = st.sidebar.date_input('Start date', datetime.date(2023, 1, 1))
    return start_date

sd = start_date_input()

def end_date_input(): #NEW
    end_date = st.sidebar.date_input('End date', datetime.date.today())
    if sd >= end_date:
        st.sidebar.error('Error: End date must fall after start date.')
    return end_date


ed = end_date_input()


def plot(): #NEW
    st.header("Historical Data")
    chart_data = pd.DataFrame(companies[chosen_company].history(start=sd, end=ed))
    chart_data = chart_data.drop("Volume", axis=1)
    chart_data = chart_data.drop("Dividends", axis=1)
    chart_data = chart_data.drop("Stock Splits", axis=1)
    st.line_chart(chart_data)
    st.header("Volume Traded")
    bar_data = pd.DataFrame(companies[chosen_company].history(start=sd, end=ed))
    bar_data = bar_data.drop("Open", axis=1)
    bar_data = bar_data.drop("Close", axis=1)
    bar_data = bar_data.drop("High", axis=1)
    bar_data = bar_data.drop("Low", axis=1)
    bar_data = bar_data.drop("Dividends", axis=1)
    bar_data = bar_data.drop("Stock Splits", axis=1)
    st.bar_chart(bar_data)


plot()