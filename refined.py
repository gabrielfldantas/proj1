from helpers import csv_export
import datetime
import pandas as pd

def fact_cotacoes():
    refined_time_series_daily = pd.read_csv("silver_data/refined_time_series_daily.csv")
    refined_time_series_daily["id"] = refined_time_series_daily.index + 1
    refined_time_series_daily["company_id"] = 1
    refined_time_series_daily.rename(
        columns={
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. volume": "volume",
            "index": "date",
        },
        inplace=True,
    )
    refined_time_series_daily = refined_time_series_daily.astype(
        {
            "open": "float64",
            "high": "float64",
            "low": "float64",
            "close": "float64",
            "volume": "int64",
        }
    )
    csv_export(refined_time_series_daily, "gold_data", "fact_cotacoes.csv")

def dim_empresa():
    df_empresa = pd.read_csv("silver_data/refined_overview.csv")
    df_empresa["company_id"] = df_empresa.index + 1
    df_empresa = df_empresa[["company_id","Symbol", "Name", "Sector", "Industry", "Country"]]
    df_empresa.columns = df_empresa.columns.str.lower()
    csv_export(df_empresa, "gold_data", "dim_empresa.csv")

# def fact_indicadores():
#     df_indicadores = pd.read_csv("silver_data/refined_overview.csv")
#     df_indicadores
#     df_indicadores = df_indicadores[["EPS","DividendPerShare", "OperatingMarginTTM", "PEGRatio"]]
#     df_indicadores["company_id"] = 1
#     df_indicadores["indicador_id"] = df_indicadores.index + 1
#     df_indicadores["tempo_id"] = datetime.datetime.now().strftime("%Y%m%d")
#     df_indicadores = df_indicadores.pivot_table(
#         index=["company_id", "indicador_id", "tempo_id"],
#         values=["EPS","DividendPerShare", "OperatingMarginTTM", "PEGRatio"],
#         aggfunc="first",
#     )
#     # df_indicadores = df_indicadores[["EPS","DividendPerShare", "OperatingMarginTTM", "PEGRatio"]]
#     # df_indicadores["indicador_fato_id"] = df_indicadores.index
#     # csv_export(df_indicadores, "gold_data", "fact_indicadores.csv")
#     print(df_indicadores)

def fact_indicadores():
    df_indicadores = pd.read_csv("silver_data/refined_overview.csv")
    df_fact_indicadores=pd.DataFrame([
        [1, datetime.datetime.now().strftime("%Y%m%d"), 1, 1, df_indicadores["EPS"][0]],
        [2, datetime.datetime.now().strftime("%Y%m%d"), 1, 2, df_indicadores["DividendPerShare"][0]],
        [3, datetime.datetime.now().strftime("%Y%m%d"), 1, 3, df_indicadores["OperatingMarginTTM"][0]],
        [4, datetime.datetime.now().strftime("%Y%m%d"), 1, 4, df_indicadores["PEGRatio"][0]],
    ], columns = ["indicador_fato_id", "tempo_id", "company_id", "indicador_id", "valor"])


    csv_export(df_fact_indicadores, "gold_data", "fact_indicadores.csv")

def dim_indicador():
    df_indicador = pd.DataFrame([
        [1, "EPS", "Earnings per share", "profitability"],
        [2, "DividendPerShare", "Amount paid to shareholders per share annually", "dividends"],
        [3, "OperatingMarginTTM", "Operating income as a percentage of revenue (TTM)", "profitability"],
        [4, "PEGRatio", "Price/earnings to growth ratio; adjusts P/E for expected growth","valuation"],
    ], columns = ["indicador_id", "nome_indicador", "descricao", "tipo"])
    csv_export(df_indicador, "gold_data", "dim_indicador.csv")
