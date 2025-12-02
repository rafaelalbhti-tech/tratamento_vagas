import pandas as pd

# Lê o JSON linha por linha
df = pd.read_json(
    r"C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\silver\vagas_.json",
    lines=True
)

# Converte a coluna 'Data' para o formato datetime
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')

# Selecionar as colunas escolhidas
colunas_interesse = ['Area', 'Empresa', 'Cidade', 'Link', 'Data']
nova_tabela = df[colunas_interesse]

#Substituir valores não informados
df['Area'] = df['Area'].replace('Não-Informado', '')

# Filtrando as vagas de dados com .contains
nova_tabela = nova_tabela[nova_tabela['Area'].str.contains('dados', case=False, na=False)]

# Salvar na gold
nova_tabela.to_json(r"C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\gold\vagas_dados_df.json",
                    orient='records', force_ascii=False, lines=True)    

print(nova_tabela.head())
