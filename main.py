from dotenv import load_dotenv
from extract import raw_time_series_daily, raw_overview
from filtered import filtered_time_series_daily, filtered_overview
from load import create_tables
from sqlalchemy import create_engine, text
import os

load_dotenv()

symbol = "AAPL"
API_KEY = os.getenv("API_KEY")

PG_URL = os.getenv("PG_URL")
PG_USERNAME = os.getenv("PG_USERNAME")
PG_PASSWORD = os.getenv("PG_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_URL}:{5432}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

csv_files = {
    "dim_empresa": "gold_data/dim_empresa.csv",
    "dim_indicador": "gold_data/dim_indicador.csv",
    "dim_tempo": "gold_data/dim_tempo.csv",
    "fact_cotacoes": "gold_data/fact_cotacoes.csv",
    "fact_indicadores": "gold_data/fact_indicadores.csv"
}


def main():
    raw_time_series_daily(symbol, API_KEY)
    raw_overview(symbol, API_KEY)
    filtered_time_series_daily()
    filtered_overview()
    create_tables(csv_files, engine)

if __name__ == "__main__":
    main()
