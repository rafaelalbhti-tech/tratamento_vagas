import pandas as pd

# Lê o JSON linha por linha
df = pd.read_json(
    r"C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\silver\vagas_.json",
    lines=True
)

# Selecionar as colunas escolhidas
colunas_interesse = ['Area', 'Empresa', 'Cidade', 'Link', 'Data']
nova_tabela = df[colunas_interesse]

# Filtrando as vagas de dados com .contains
nova_tabela = nova_tabela[nova_tabela['Area'].str.contains('Dados', case=False, na=False)]

# Salvar na gold
nova_tabela.to_json(r"C:\Users\albuq\Desktop\projetos_avulsos\tratamento_vagas\gold\vagas_dados_df.json",
                    orient='records', force_ascii=False, lines=True)
