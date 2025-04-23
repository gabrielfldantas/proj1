import pandas as pd
from sqlalchemy import create_engine, text

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