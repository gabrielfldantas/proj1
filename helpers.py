import requests as req
import os


def get_request(func, symb, key):
    url = f"https://www.alphavantage.co/query"
    params = {"function": func, "symbol": symb, "apikey": key}
    return req.get(url, params=params).json()


def csv_export(df, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    df.to_csv(path, index=False)
    print(f"Exported {filename}")
