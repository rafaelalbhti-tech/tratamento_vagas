import pandas as pd
from datetime import datetime
from pathlib import Path


# Define a pasta raiz do projeto automaticamente
ROOT_DIR = Path(__file__).parent


#caminhos ralativos baseados na raiz
caminho_gold = ROOT_DIR / 'gold' / 'filtros_applied_gold.py'
df = pd.read_json(caminho_gold, lines=True)


#Conta a quantidade de vagas por cidade
vagas_por_cidade = df['Cidade'].value_counts().reset_index()
vagas_por_cidade.columns = ['Cidade', 'quantidade_total_vagas']


#Conta a quantidade de vagas por data
vagas_por_data = df['Data'].value_counts().reset_index()
vagas_por_data.columns = ['Data', 'quantidade_total_vagas_data']


# Caminho de Saída
#Exportar os dfs de insights para csv e depois para o power bi
pasta_insights = ROOT_DIR / 'insights'

# Salvando
vagas_por_cidade.to_csv(pasta_insights / 'vagas_por_cidade.csv', index=False)
vagas_por_data.to_csv(pasta_insights / 'vagas_por_data.csv', index=False)


#Faz o merge do dataframe original com o dataframe de contagem de vagas por cidade
df_final = df.merge(vagas_por_cidade, on ='Cidade', how='left')
df_final = df_final.merge(vagas_por_data, on='Data', how='left')


#convertendo object para datetime
df_final['Data'] = pd.to_datetime(df_final['Data'], format='%d/%m/%Y')


#cria a coluna mes_referencia para agrupar as vagas
df['mes_referencia'] = df_final['Data'].dt.to_period('M')


#agrupa as vagas por mês
df_agrupado = df.groupby('mes_referencia').size().reset_index(name='quantidade_total_vagas_mes')


