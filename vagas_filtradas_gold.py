import pandas as pd

# Lê o JSON linha por linha
df = pd.read_json(
    r"C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\silver\vagas_.json",
    lines=True
)

# Filtrando as vagas de dados com .contains
df = df[df['Area'].str.contains('dados', case=False, na=False)]

# Salvar na gold
df.to_json(r"C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\gold\vagas_dados_df.json",
                    orient='records', force_ascii=False, lines=True)    

print(df.head())
