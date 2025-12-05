import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).parent

caminho_entrada = ROOT_DIR / 'silver' / 'vagas_tratadas.json'
caminho_saida = ROOT_DIR / 'gold' / 'vagas_dados_gold.json'

df = pd.read_json(caminho_entrada, lines=True)

# Filtrando as vagas de dados com .contains
df = df[df['Area'].str.contains('dados', case=False, na=False)]


# Salvando o arquivo filtrado na camada gold
df.to_json(caminho_saida, orient='records', force_ascii=False, lines=True)

print("Arquivo salvo com sucesso na pasta gold!")
