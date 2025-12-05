# 📊 Data Jobs Analytics: Pipeline de Dados & Dashboard

> **Análise do mercado de estágios em Dados**

Este projeto consiste em uma pipeline de engenharia de dados completa (ETL) que coleta, processa e visualiza dados de vagas de emprego. O objetivo é transformar dados brutos de planilhas em insights estratégicos sobre frequência e geografia das vagas, utilizando a arquitetura **Medalhão (Bronze, Silver, Gold)**.

---

## 🖼️ Visão Geral do Dashboard

![Dashboard Overview]
(assets/dashboard_vagas.png)
(assets/dashboard_analise_temporal.png)

**Principais Insights:**
* **Geografia:** Mapeamento das cidades com maior concentração de oportunidades.
* **Sazonalidade:** Análise temporal para identificar os meses com picos de novas vagas.
* **KPIs:** Monitoramento de volume total e recordes de postagens.


## 🏗️ Arquitetura do Projeto

O projeto segue os princípios da **Arquitetura Medalhão** para garantir a qualidade e rastreabilidade dos dados:

tratamento_vagas/ 
    ├── raw/
    │   └── vagas.xlsx
    |
    ├── bronze/
    │   └── vagas.json
    |
    ├── silver/
    │   └── vagas_.json
    |
    ├── gold/
    │   └── vagas_dados_gold.json
    |
    ├── insights
    |    ├── vagas_por_cidade.csv
    |    |    └── dashboard_vagas_cidade.pbix
    |    └── vagas_por_data.csv
    |         └── dashboard_analise-temporal.pbix
    |
    ├── xlsx_to_json_bronze.py
    ├── json_reader_silver.py
    └── filtros_applied_gold.py
    └── insights.py

____________________________________________________________________________________________________
🧱 Arquitetura do Pipeline (Medallion)
    
1. 🥉 Camada Bronze (Raw)
Input: Arquivos Excel (.xlsx) manuais ou extraídos.
Processo: Conversão para JSON para facilitar leitura e histórico.
Script: xlsx_to_json_bronze.py


2. 🥈 Camada Silver (Cleansed)

Processo: Tratamento de qualidade de dados.
Conversão de tipos (Datetime, String).
Remoção de duplicatas e nulos.
Padronização de nomes de cidades (ex: "SJC" -> "São José dos Campos").
Script: json_reader_silver.py


3. 🥇 Camada Gold (Curated)

Processo: Aplicação de regras de negócio.
Filtragem por palavras-chave específicas da área de dados.
Enriquecimento e estruturação final.
Script: filtros_applied_gold.py


4. 📈 Camada Insights (Consumption)

Processo: Geração de tabelas dimensão e fato otimizadas para o Power BI.
vagas_por_cidade.csv
vagas_por_mes.csv
Script: insights.py


🛠️ Aplicações técnicas:

Linguagem: Python
Bibliotecas: Pandas, OpenPyXL, OS, Json, Datetime.
Visualização: Microsoft Power BI.
Conceitos: ETL, Data Cleaning, Data Modeling, Time Series Analysis.
____________________________________________________________________________________________________
🚀 Como Executar Localmente

1. Clone o repositório:

    git clone [https://github.com/rafaelalbhti-tech/tratamento_vagas.git](https://github.com/rafaelalbhti-tech/tratamento_vagas.git)
    cd tratamento_vagas

2. Instale as depêndencias:

    pip install pandas openpyxl

3. Execute a pipeline na ordem:

    # 1. Ingestão dos dados brutos
    python xlsx_to_json_bronze.py

    # 2. Tratamento e Limpeza
    python json_reader_silver.py

    # 3. Refinamento Gold
    python filtros_applied_gold.py

    # 4. Geração de Insights para BI
    python insights.py

4. Abra o Dashboard:

    Abra o arquivo .pbix na pasta insights com o Power BI Desktop e atualize os dados.
____________________________________________________________________________________________________
 Contato
Rafael Albuquerque

📞(11) 96207-0699
LinkedIn: https://br.linkedin.com/in/rafael-albuquerque-47a621249
____________________________________________________________________________________________________
Este projeto foi desenvolvido como parte de um estudo prático sobre Engenharia de Dados e Business Intelligence.


Link da planilha em tempo real: https://docs.google.com/spreadsheets/d/13lutgdWIY7ezc-6PihVQcjWaqsdk0Pb-SBIEDpHx9as/edit?usp=sharing
