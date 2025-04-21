from helpers import csv_export
import pandas as pd
import json


def filtered_time_series_daily():
    with open("bronze_data/raw_time_series_daily.json") as f:
        data = json.load(f)
    daily_data = data.get("Time Series (Daily)", {})
    refined_time_series_daily = pd.DataFrame.from_dict(daily_data, orient="index")
    refined_time_series_daily.reset_index(inplace=True)
    refined_time_series_daily.rename(columns={"index": "date"},inplace=True)
    csv_export(refined_time_series_daily, "silver_data", "refined_time_series_daily.csv")


def filtered_overview():
    df_overview = pd.read_json("bronze_data/raw_overview.json", orient="index").T
    csv_export(df_overview, "silver_data", "refined_overview.csv")



filtered_time_series_daily()