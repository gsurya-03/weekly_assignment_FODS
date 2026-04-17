"""
this program calculates bmi and assigns health status
it adds new columns to dataframe
"""

import pandas as pd

def get_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi <= 24.9:
        return "healthy"
    elif 25 <= bmi <= 29.9:
        return "overweight"
    elif 30 <= bmi <= 34.9:
        return "high risk"
    else:
        return "critical"


def process_data(df):
    df["BMI"] = df["weight"] / df["height"]
    df["Health_Status"] = df["BMI"].apply(get_status)
    print(df)


def main():
    try:
        df = pd.read_csv("health_data.csv")
        process_data(df)
    except FileNotFoundError:
        print("csv file not found")


if __name__ == "__main__":
    main()