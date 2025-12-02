import pandas as pd


# lê o arquivo csv na origem
df = pd.read_csv(r'C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\raw\vagas.csv')

# converte e salva como json no destino
df.to_json(r'C:\Users\albuq\\Desktop\projetos_avulsos\tratamento_vagas\bronze\vagas.json', orient='records', lines=True)