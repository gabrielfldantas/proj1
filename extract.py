from helpers import get_request
import json

def raw_time_series_daily(symbol, key):
    time_series_daily = get_request("TIME_SERIES_DAILY", symbol, key)
    with open("bronze_data/raw_time_series_daily.json", "w", encoding="utf-8") as f:
        json.dump(time_series_daily, f, ensure_ascii=False, indent=4)


def raw_overview(symbol, key):
    overview = get_request("OVERVIEW", symbol, key)
    with open("bronze_data/raw_overview.json", "w", encoding="utf-8") as f:
        json.dump(overview, f, ensure_ascii=False, indent=4)
