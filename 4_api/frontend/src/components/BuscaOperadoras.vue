<template>
  <div class="busca-operadoras">
    <div class="search-container">
      <input
        v-model="termoBusca"
        @input="buscarOperadoras"
        type="text"
        placeholder="Digite o nome, registro ANS ou CNPJ da operadora..."
        class="search-input"
      />
    </div>

    <div v-if="loading" class="loading">
      Carregando...
    </div>

    <div v-else-if="erro" class="erro">
      {{ erro }}
    </div>

    <div v-else-if="operadoras.length > 0" class="resultados">
      <div v-for="operadora in operadoras" :key="operadora.registro_ans" class="operadora-card">
        <h3>{{ operadora.razao_social }}</h3>
        <p v-if="operadora.nome_fantasia">Nome Fantasia: {{ operadora.nome_fantasia }}</p>
        <p>Registro ANS: {{ operadora.registro_ans }}</p>
        <p>CNPJ: {{ operadora.cnpj }}</p>
        <p>{{ operadora.cidade }} - {{ operadora.uf }}</p>
      </div>
    </div>

    <div v-else-if="termoBusca" class="sem-resultados">
      Nenhuma operadora encontrada para o termo "{{ termoBusca }}"
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'BuscaOperadoras',
  data() {
    return {
      termoBusca: '',
      operadoras: [],
      loading: false,
      erro: null
    }
  },
  methods: {
    async buscarOperadoras() {
      if (!this.termoBusca) {
        this.operadoras = [];
        return;
      }

      this.loading = true;
      this.erro = null;

      try {
        const response = await axios.get(`/api/operadoras/busca?q=${this.termoBusca}`);
        this.operadoras = response.data.operadoras;
      } catch (error) {
        this.erro = 'Erro ao buscar operadoras. Por favor, tente novamente.';
        console.error('Erro:', error);
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.busca-operadoras {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.search-container {
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 2px solid #ddd;
  border-radius: 8px;
  outline: none;
  transition: border-color 0.3s;
}

.search-input:focus {
  border-color: #4CAF50;
}

.loading, .erro, .sem-resultados {
  text-align: center;
  padding: 20px;
  color: #666;
}

.erro {
  color: #f44336;
}

.operadora-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s;
}

.operadora-card:hover {
  transform: translateY(-2px);
}

.operadora-card h3 {
  margin: 0 0 10px 0;
  color: #333;
}

.operadora-card p {
  margin: 5px 0;
  color: #666;
}
</style> 