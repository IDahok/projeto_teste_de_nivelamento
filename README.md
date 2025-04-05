# Projeto Intuitive - Sistema de Análise de Operadoras de Saúde

Este projeto consiste em um sistema completo para coleta, processamento, armazenamento e visualização de dados de operadoras de saúde, com foco na análise de demonstrações contábeis.

## Estrutura do Projeto

O projeto está organizado em 4 pastas principais, cada uma com uma função específica:

### 1. Web Scraping (`1_web_scraping/`)
- **Função**: Coleta de dados da web
- **Arquivos principais**:
  - `baixar_anexos.py`: Script para baixar automaticamente os anexos do site da ANS
  - `Anexo_I.pdf` e `Anexo_II.pdf`: Documentos baixados do site da ANS
  - `ANEXOS_COMPACTADOS.zip`: Arquivo compactado com os anexos

### 2. Transformação de Dados (`2_transformacao_de_dados/`)
- **Função**: Processamento e transformação dos dados coletados
- **Arquivos principais**:
  - `extrair_tabela.py`: Script para extrair tabelas de PDF e converter para CSV
  - `rol_procedimentos.csv`: Dados extraídos do PDF em formato CSV
  - `Teste_Jonatas_Henrique.zip`: Arquivo compactado com os resultados

### 3. Banco de Dados (`3_banco_de_dados/`)
- **Função**: Armazenamento e consulta dos dados
- **Arquivos principais**:
  - `scripts_sql/01_criacao_tabelas.sql`: Script para criar as tabelas no banco de dados
  - `scripts_sql/02_importacao_dados.sql`: Script para importar dados CSV para o banco
  - `scripts_sql/03_consultas_analiticas.sql`: Consultas SQL para análise dos dados
  - `dados/`: Pasta com arquivos CSV para importação

### 4. API e Frontend (`4_api/`)
- **Função**: Interface web para interação com os dados
- **Arquivos principais**:
  - `app.py`: Servidor Flask que fornece a API REST
  - `frontend/`: Aplicação Vue.js para interface do usuário
    - `src/components/BuscaOperadoras.vue`: Componente para busca de operadoras
    - `src/App.vue`: Componente principal da aplicação
    - `index.html`: Página HTML principal

## Funcionalidades

1. **Coleta de Dados**: Download automático de documentos da ANS
2. **Processamento**: Extração de tabelas de PDF para CSV
3. **Armazenamento**: Banco de dados PostgreSQL para armazenar os dados
4. **Análise**: Consultas SQL para análise de demonstrações contábeis
5. **Interface Web**: Busca textual de operadoras com resultados em tempo real

## Tecnologias Utilizadas

- **Backend**: Python, Flask, PostgreSQL
- **Frontend**: Vue.js, Axios
- **Processamento de Dados**: Pandas, PDFPlumber
- **Web Scraping**: BeautifulSoup, Requests

## Como Executar

1. **Configuração do Ambiente**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Banco de Dados**:
   ```bash
   psql -U postgres -d postgres -f 3_banco_de_dados/scripts_sql/01_criacao_tabelas.sql
   ```

3. **API e Frontend**:
   ```bash
   cd 4_api
   python app.py
   ```

4. **Acessar a Aplicação**:
   Abra o navegador e acesse `http://localhost:5000` 