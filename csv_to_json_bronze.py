import pandas as pd


# lê o arquivo csv na origem
dfs = pd.read_excel(r'C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\raw\vagas.xlsx', sheet_name=None)

#transforma o dicionario de dataframes em um dataframe
df = pd.concat(dfs.values(), ignore_index=True)

# converte e salva como json no destino
df.to_json(r'C:\Users\albuq\\Desktop\projetos_avulsos\tratamento_vagas\bronze\vagas.json', orient='records', lines=True)