-- 10 operadoras com maiores despesas no último trimestre
SELECT 
    o.razao_social,
    o.nome_fantasia,
    REPLACE(REPLACE(d.vl_saldo_final,'.',''),',','.')::float
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_ativas o ON d.reg_ans = o.registro_ans
WHERE 
    d.data = '2024-10-01'
    AND
    CD_CONTA_CONTABIL::numeric = 411
GROUP BY 
    o.razao_social, o.nome_fantasia, REPLACE(REPLACE(d.vl_saldo_final,'.',''),',','.')::float
ORDER BY 
    REPLACE(REPLACE(d.vl_saldo_final,'.',''),',','.')::float DESC
LIMIT 10;

-- 10 operadoras com maiores despesas no último ano
SELECT 
    o.razao_social,
    o.nome_fantasia,
    SUM(REPLACE(REPLACE(d.vl_saldo_final,'.',''),',','.')::float)
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_ativas o ON d.reg_ans = o.registro_ans
WHERE 
    d.data::date between '2024-01-01' and '2024-12-31'
    AND
    CD_CONTA_CONTABIL::numeric = 411
    AND
    REPLACE(REPLACE(d.vl_saldo_final,'.',''),',','.')::float > 0
GROUP BY 
    o.razao_social, o.nome_fantasia
ORDER BY 
    SUM(REPLACE(REPLACE(d.vl_saldo_final,'.',''),',','.')::float) DESC
LIMIT 10;
