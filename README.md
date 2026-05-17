Gerenciador de Gastos Pessoais
Mostrar Imagem
🔗 Deploy

Aplicação publicada: adicione aqui o link do Vercel/Render/GitHub Pages após o deploy


Descrição do problema
Muitas pessoas perdem o controle dos próprios gastos por falta de um registro simples e acessível. Sem visibilidade sobre onde o dinheiro é gasto, fica difícil economizar ou identificar despesas desnecessárias — problema especialmente comum entre jovens adultos e trabalhadores autônomos.
Proposta da solução
Uma aplicação CLI leve e direta que permite registrar, categorizar e visualizar gastos pessoais, com resumo por categoria e total acumulado. Ao iniciar, a aplicação consulta a cotação atual do dólar (via AwesomeAPI) e exibe o valor para o usuário.
Público-alvo
Qualquer pessoa que queira controlar seus gastos de forma simples, diretamente pelo terminal.
Funcionalidades

Exibir cotação atual do dólar (USD → BRL) ao iniciar
Adicionar gasto com descrição, valor e categoria
Listar todos os gastos registrados
Filtrar gastos por categoria
Ver resumo visual com total por categoria e percentual
Remover um gasto pelo ID

Tecnologias utilizadas

Python 3.9+
requests — consumo de API REST externa
pytest — testes automatizados (unitários + integração)
ruff — linting e análise estática
GitHub Actions — integração contínua (CI)

API Pública utilizada
APIEndpointDados retornadosAwesomeAPI EconomiaGET https://economia.awesomeapi.com.br/json/last/USD-BRLCotação atual do dólar em reais
Instalação
bashgit clone https://github.com/Renatatxr19/Gastos-Pessoais
cd Gastos-Pessoais
git checkout entrega-intermediaria
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
Execução
bashpython -m src.app
Exemplo de sessão:
==========================================
   💰  GERENCIADOR DE GASTOS PESSOAIS
==========================================
   💵  Dólar hoje: R$ 5.25
==========================================

------------------------------------------
  1. Adicionar gasto
  2. Listar todos os gastos
  3. Listar por categoria
  4. Resumo por categoria
  5. Remover gasto
  0. Sair
------------------------------------------
  Escolha uma opção:
Rodando os testes
bash# Todos os testes (unitários + integração mock):
pytest tests/ -v

# Apenas testes de integração real (requer internet):
pytest tests/ -v -m integration

# Pular testes de integração real (modo offline/CI):
pytest tests/ -v -m "not integration"
Rodando o lint
bashruff check src/
Versão atual
2.0.0
Autor
Renata Teixeira - renata.teixeira@sempreceub.com
Repositório
https://github.com/Renatatxr19/Gastos-Pessoais