import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

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

def create_tables(csv_files, engine):
    for table_name, file_path in csv_files.items():
        print(f"\n Carregando dados para a tabela `{table_name}`...")

        # Lê o CSV
        df = pd.read_csv(file_path)

        # Limpa a tabela antes de inserir (sem derrubar estrutura)
        with engine.begin() as conn:
            print(f" Limpando tabela `{table_name}`...")
            conn.execute(text(f"DELETE FROM {table_name}"))

        # Insere os dados
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f" Tabela `{table_name}` atualizada com sucesso!")

if __name__ == "__main__":
    print(" Iniciando carga dos dados no banco PostgreSQL...\n")
    create_tables(csv_files, engine)
    print("\n Carga finalizada com sucesso!")