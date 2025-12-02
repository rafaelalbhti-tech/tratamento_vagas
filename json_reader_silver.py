import pandas as pd

#Lendo o arquivo json
df = pd.read_json(
    r'C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\bronze\vagas.json',
    lines=True
    )

#renomeando a coluna
df.rename(columns={'Data de Inclus\u00e3o': 'Data'}, inplace=True)

#filtrando apenas as colunas de interesse
colunas_interesse = ['Area', 'Empresa', 'Cidade', 'Link', 'Data']

#Criando o dataframe filtrado
df_filtrado = df[colunas_interesse].copy()

df_filtrado['Data'] = pd.to_datetime(df_filtrado['Data'], unit='ms', errors='coerce')
df_filtrado['Data'] = df_filtrado['Data'].dt.strftime('%d/%m/%Y')

df = df_filtrado

#Salvando o df filtrado
df.to_json(r'C:\Users\\albuq\Desktop\projetos_avulsos\tratamento_vagas\silver\vagas_.json', orient='records', lines=True)

print(df.head())