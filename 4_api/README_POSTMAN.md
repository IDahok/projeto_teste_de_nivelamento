# Coleção Postman para API de Operadoras de Saúde

Este documento descreve como usar a coleção do Postman para testar a API de busca de operadoras de saúde desenvolvida no projeto.

## Como Importar a Coleção

1. Abra o Postman
2. Clique em "Import" no canto superior esquerdo
3. Selecione o arquivo `postman_collection.json` localizado na pasta `4_api`
4. Clique em "Import" para adicionar a coleção ao seu workspace

## Estrutura da Coleção

A coleção está organizada em três pastas principais:

### 1. Busca de Operadoras

Contém exemplos de requisições para buscar operadoras por diferentes critérios:

- **Buscar por Razão Social**: Exemplo de busca pelo termo "Saúde"
- **Buscar por Registro ANS**: Exemplo de busca pelo registro "123456"
- **Buscar por CNPJ**: Exemplo de busca pelo CNPJ "12.345.678"
- **Buscar por Cidade**: Exemplo de busca pela cidade "São Paulo"
- **Busca sem Resultados**: Exemplo de busca que não retorna resultados

### 2. Teste de Banco de Dados

Contém uma requisição para testar a conexão com o banco de dados:

- **Testar Conexão**: Verifica se a API está conectada corretamente ao banco de dados

### 3. Frontend

Contém uma requisição para acessar o frontend:

- **Página Principal**: Acessa a página principal do frontend

## Como Usar a Coleção

1. Certifique-se de que o servidor Flask está rodando:
   ```bash
   cd 4_api
   python app.py
   ```

2. No Postman, selecione uma das requisições da coleção

3. Clique em "Send" para enviar a requisição

4. Verifique a resposta no painel inferior

## Exemplos de Respostas

### Busca por Razão Social

```json
{
  "operadoras": [
    {
      "razao_social": "Operadora Saúde Exemplo 1",
      "nome_fantasia": "Saúde Exemplo 1",
      "registro_ans": "123456",
      "cnpj": "12.345.678/0001-90",
      "cidade": "São Paulo",
      "uf": "SP"
    },
    {
      "razao_social": "Operadora Saúde Exemplo 2",
      "nome_fantasia": "Saúde Exemplo 2",
      "registro_ans": "234567",
      "cnpj": "23.456.789/0001-91",
      "cidade": "Rio de Janeiro",
      "uf": "RJ"
    },
    {
      "razao_social": "Operadora Saúde Exemplo 3",
      "nome_fantasia": "Saúde Exemplo 3",
      "registro_ans": "345678",
      "cnpj": "34.567.890/0001-92",
      "cidade": "Belo Horizonte",
      "uf": "MG"
    }
  ]
}
```

### Teste de Conexão com o Banco de Dados

```json
{
  "status": "success",
  "message": "Conexão com o banco de dados estabelecida com sucesso!",
  "version": "PostgreSQL 15.3 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 12.2.0, 64-bit"
}
```

## Endpoints Disponíveis

1. **Busca de Operadoras**
   - URL: `http://localhost:5000/api/operadoras/busca`
   - Método: GET
   - Parâmetros:
     - `q`: Termo de busca (obrigatório)

2. **Teste de Banco de Dados**
   - URL: `http://localhost:5000/test-db`
   - Método: GET

3. **Frontend**
   - URL: `http://localhost:5000/`
   - Método: GET

## Personalização

Você pode personalizar as requisições alterando os parâmetros de busca:

1. Selecione uma requisição de busca
2. Na aba "Params", altere o valor do parâmetro "q"
3. Clique em "Send" para enviar a requisição com o novo parâmetro

## Solução de Problemas

Se você encontrar problemas ao usar a coleção:

1. Verifique se o servidor Flask está rodando
2. Verifique se o banco de dados PostgreSQL está acessível
3. Verifique se as tabelas foram criadas corretamente
4. Verifique os logs do servidor Flask para identificar possíveis erros 