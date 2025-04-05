from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
import logging

# Configuração de logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Carrega as variáveis de ambiente
load_dotenv()

# Imprime as variáveis de ambiente para debug
logger.info("=== Configurações do Banco de Dados ===")
logger.info(f"DB_HOST: {os.getenv('DB_HOST')}")
logger.info(f"DB_NAME: {os.getenv('DB_NAME')}")
logger.info(f"DB_USER: {os.getenv('DB_USER')}")
logger.info(f"DB_PASSWORD: {'*' * len(os.getenv('DB_PASSWORD', ''))}")
logger.info("=====================================")

app = Flask(__name__, static_folder='frontend/dist', static_url_path='')
CORS(app)

def get_db_connection():
    try:
        logger.info("\nTentando conectar ao banco de dados...")
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        logger.info("✅ Conexão estabelecida com sucesso!")
        return conn
    except Exception as e:
        logger.error(f"❌ Erro ao conectar ao banco de dados: {str(e)}")
        raise e

@app.route('/test-db')
def test_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({
            'status': 'success',
            'message': 'Conexão com o banco de dados estabelecida com sucesso!',
            'version': version[0]
        })
    except Exception as e:
        logger.error(f"Erro na rota test-db: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/operadoras/busca', methods=['GET'])
def buscar_operadoras():
    termo_busca = request.args.get('q', '')
    
    if not termo_busca:
        return jsonify({'error': 'Termo de busca é obrigatório'}), 400
    
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        query = """
        SELECT 
            o.razao_social,
            o.nome_fantasia,
            o.registro_ans,
            o.cnpj,
            o.cidade,
            o.uf
        FROM 
            operadoras_ativas o
        WHERE 
            o.razao_social ILIKE %s 
            OR o.nome_fantasia ILIKE %s
            OR o.registro_ans ILIKE %s
            OR o.cnpj ILIKE %s
        LIMIT 10
        """
        
        termo_busca = f'%{termo_busca}%'
        logger.info(f"Executando busca com o termo: {termo_busca}")
        cur.execute(query, (termo_busca, termo_busca, termo_busca, termo_busca))
        
        resultados = cur.fetchall()
        logger.info(f"Encontrados {len(resultados)} resultados")
        
        cur.close()
        conn.close()
        
        return jsonify({
            'operadoras': [dict(row) for row in resultados]
        })
        
    except Exception as e:
        logger.error(f"Erro durante a busca: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("Iniciando o servidor Flask...")
    app.run(host='0.0.0.0', port=5000, debug=True) 