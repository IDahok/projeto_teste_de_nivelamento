import requests
from bs4 import BeautifulSoup
import zipfile

# Passo 1: Acessar o site
print("Acessando o site...")
pagina = requests.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
conteudo = BeautifulSoup(pagina.text, 'html.parser')

# Passo 2: Procurar os anexos
print("Procurando Anexo I e Anexo II...")
arquivos = []
for anexo in ['Anexo I', 'Anexo II']:
    link = conteudo.find('a', string=lambda t: t and anexo in t)
    if link:
        nome_arquivo = anexo.replace(' ', '_') + '.pdf'
        print(f"Baixando {nome_arquivo}...")
        pdf = requests.get(link['href']).content
        with open(nome_arquivo, 'wb') as f:
            f.write(pdf)
        arquivos.append(nome_arquivo)

# Passo 3: Juntar tudo em um ZIP
if arquivos:
    print("Criando arquivo compactado...")
    with zipfile.ZipFile('ANEXOS_COMPACTADOS.zip', 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo)
    print("Pronto! Arquivo 'ANEXOS_COMPACTADOS.zip' criado com sucesso!")
else:
    print("Não foram encontrados os anexos no site.")