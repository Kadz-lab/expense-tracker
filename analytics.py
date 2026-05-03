import pandas as pd

def load_data(data):
    df = pd.DataFrame(data, columns=["Date","Amount","Category","Description"])
    return df

def category_chart(df):
    return df.groupby("Category")["Amount"].sum()

def monthly_chart(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    return df.groupby("Month")["Amount"].sum()