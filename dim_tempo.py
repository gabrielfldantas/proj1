from helpers import csv_export
import datetime
import pandas as pd


def date_info(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    year = date.year
    month = date.month
    day = date.day
    quarter = (date.month - 1) // 3 + 1
    tempo_id = date.strftime("%Y%m%d")
    return tempo_id, date, day, month, year, quarter


def dim_tempo_creator():
    data = []
    i = -1000
    while i < 1000:
        end_date = datetime.datetime.now() + datetime.timedelta(days=i)
        i += 1
        end_date = end_date.strftime("%Y-%m-%d")
        tempo_id, date, day, month, year, quarter = date_info(end_date)
        data.append(
            {
                "tempo_id": tempo_id,
                "date": date,
                "day": day,
                "month": month,
                "year": year,
                "quarter": quarter,
            }
        )
    df_dim_date = pd.DataFrame(data)
    csv_export(df_dim_date, "gold_data", "dim_tempo.csv")


dim_tempo_creator()
