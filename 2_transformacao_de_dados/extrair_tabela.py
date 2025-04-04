import os
import pdfplumber
import pandas as pd
import zipfile

# 1. Configuração dos caminhos
pasta_script = os.path.dirname(__file__)
pasta_raiz = os.path.dirname(pasta_script)

# Caminho do PDF
pdf_path = os.path.join(pasta_raiz, '1_web_scraping', 'Anexo_I.pdf')

# 2. Verificação do arquivo
if not os.path.exists(pdf_path):
    print("ERRO: Arquivo não encontrado!")
    print(f"Coloque o arquivo em: {os.path.join(pasta_raiz, '1_web_scraping')}")
    exit()

# 3. Processamento PASSO-A-PASSO
print("Extraindo dados do PDF...")
todos_dados = []

# Abre o PDF e pega as tabelas
with pdfplumber.open(pdf_path) as pdf:
    for pagina in pdf.pages:
        tabela = pagina.extract_table()
        if tabela:
            todos_dados.extend(tabela)

# Organiza os dados
cabecalhos = todos_dados[0]  
dados = todos_dados[1:]      

# Cria a tabela e ajusta os nomes
tabela_final = pd.DataFrame(dados, columns=cabecalhos)
tabela_final.columns = [col.replace('OD', 'Odontológico')
                       .replace('AMB', 'Ambulatorial') 
                       for col in tabela_final.columns]

# 4. Salva os resultados (NA PASTA ATUAL)
csv_path = 'rol_procedimentos.csv'
zip_path = 'Teste_Jonatas_Henrique.zip'

tabela_final.to_csv(csv_path, index=False)

# Cria o ZIP
with zipfile.ZipFile(zip_path, 'w') as zip_file:
    zip_file.write(csv_path)

print("Concluído com sucesso!")
print(f"Arquivos criados na pasta: {pasta_script}")
print(f"- {csv_path}")
print(f"- {zip_path}")