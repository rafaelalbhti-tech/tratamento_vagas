import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).parent

#Lê o arquivo json na camada silver
caminho_entrada = ROOT_DIR / 'bronze' / 'vagas.json'
caminho_saida = ROOT_DIR / 'silver' / 'vagas_tratadas.json'
df = pd.read_json(caminho_entrada, lines=True)

#renomeando a coluna
df.rename(columns={'Data de Inclusão': 'Data'}, inplace=True)

#Substituindo valores indesejados
df = df[df['Cidade'] != 'Não-informado']
df = df.replace('SJC', 'São José dos Campos',)
df = df.replace('Santo andré', 'Santo André')
df = df[df['Cidade'] != 'Remoto']

#filtrando apenas as colunas de interesse
colunas_interesse = ['Area', 'Empresa', 'Cidade', 'Link', 'Data']

#Criando o dataframe filtrado
df_filtrado = df[colunas_interesse].copy()

#convertendo data para datetime
df_filtrado['Data'] = pd.to_datetime(df_filtrado['Data'], unit='ms', errors='coerce')
df_filtrado['Data'] = df_filtrado['Data'].dt.strftime('%d/%m/%Y')

#Salvando o df filtrado
df.to_json(caminho_saida, orient='records', force_ascii=False, lines=True)
print("Arquivo salvo com sucesso na pasta silver!")