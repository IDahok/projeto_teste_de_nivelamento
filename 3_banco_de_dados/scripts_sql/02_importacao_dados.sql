-- IMPORTAR OPERADORAS (Relatorio_cadop.csv)
COPY operadoras_ativas(registro_ans,
cnpj,
razao_social,
nome_fantasia,
modalidade,
logradouro,
numero,
complemento,
bairro,
cidade,
uf,
cep,
ddd,
telefone,
fax,
endereco_eletronico,
representante,
cargo_representante,
regiao_comercializacao,
data_registro_ans)
FROM '/srv/arquivocsv/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER;

-- IMPORTAR DADOS TRIMESTRAIS
COPY demonstracoes_contabeis(data,
reg_ans,
cd_conta_contabil,
descricao,
vl_saldo_inicial,
vl_saldo_final)
FROM '/srv/arquivocsv/dados/1T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis(data,
reg_ans,
cd_conta_contabil,
descricao,
vl_saldo_inicial,
vl_saldo_final)
FROM '/srv/arquivocsv/dados/2T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis(data,
reg_ans,
cd_conta_contabil,
descricao,
vl_saldo_inicial,
vl_saldo_final)
FROM '/srv/arquivocsv/dados/3T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis(data,
reg_ans,
cd_conta_contabil,
descricao,
vl_saldo_inicial,
vl_saldo_final)
FROM '/srv/arquivocsv/dados/4T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis(data,
reg_ans,
cd_conta_contabil,
descricao,
vl_saldo_inicial,
vl_saldo_final)
FROM '/srv/arquivocsv/dados/1T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis(data,
reg_ans,
cd_conta_contabil,
descricao,
vl_saldo_inicial,
vl_saldo_final)
FROM '/srv/arquivocsv/dados/2T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis(data,
reg_ans,
cd_conta_contabil,
descricao,
vl_saldo_inicial,
vl_saldo_final)
FROM '/srv/arquivocsv/dados/3T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY desmostracoes_contabeis(data,
reg_ans,
cd_conta_contabil,
descricao,
vl_saldo_inicial,
vl_saldo_final)
FROM '/srv/arquivocsv/dados/4T2024.csv'
DELIMITER ';'
CSV HEADER;