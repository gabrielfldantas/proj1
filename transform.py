from helpers import csv_export
import pandas as pd

refined_time_series_daily = "silver_data/refined_time_series_daily.csv"
refined_overview = "silver_data/refined_overview.csv"

def fact_cotacao(input_file: str):
    fact_cotacao = pd.read_csv(input_file)
    csv_export(fact_cotacao, "gold_data", "fact_cotacao.csv")

def dim_empresa(input_file: str):
    dim_empresa = pd.read_csv(input_file)
    dim_empresa["company_id"] = dim_empresa.index + 1
    dim_empresa = dim_empresa[["company_id","Symbol", "Name", "Sector", "Industry", "Country"]]
    dim_empresa.columns = dim_empresa.columns.str.lower()
    csv_export(dim_empresa, "gold_data", "dim_empresa.csv")
    

dim_empresa(refined_overview)