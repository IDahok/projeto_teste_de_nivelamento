<template>
  <div id="app">
    <header>
      <h1>Busca de Operadoras de Saúde</h1>
    </header>
    <main>
      <BuscaOperadoras />
    </main>
  </div>
</template>

<script>
import BuscaOperadoras from './components/BuscaOperadoras.vue'

export default {
  name: 'App',
  components: {
    BuscaOperadoras
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
  padding: 0;
  min-height: 100vh;
  background-color: #f5f5f5;
}

header {
  background-color: #4CAF50;
  color: white;
  padding: 20px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
  margin: 0;
  font-size: 24px;
}

main {
  padding: 20px;
}
</style> 