import pandas as pd
from datetime import datetime
import os
from pathlib import Path

# Define a pasta raiz do projeto automaticamente
# Isso pega a pasta onde o script 'xlsx_to_json_bronze.py' está salvo
ROOT_DIR = Path(__file__).parent 

# 3. Define os caminhos relativos baseados na raiz
caminho_entrada = ROOT_DIR / 'raw' / 'vagas.xlsx'
caminho_saida = ROOT_DIR / 'bronze' / 'vagas.json'

# Lê o arquivo Excel
dfs = pd.read_excel(caminho_entrada, sheet_name=None)

#Junta as abas do arquivo num unico df
df = pd.concat(dfs.values(), ignore_index=True)

# adiciona a coluna de data de ingestão
df["data_ingestao"] = datetime.now().isoformat()

# converte e salva como json no destino
df.to_json(caminho_saida, orient='records', force_ascii=False, lines=True)
print('Arquivo salvo com sucesso na pasta bronze!')