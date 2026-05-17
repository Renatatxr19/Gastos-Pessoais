# 💰 Gerenciador de Gastos Pessoais

---

## 🔗 Deploy

Aplicação publicada: *(adicione aqui o link do deploy quando disponível — Vercel/Render/etc.)*

---

## 📌 Descrição do problema

Muitas pessoas perdem o controle dos próprios gastos por falta de um registro simples e acessível. Sem visibilidade sobre onde o dinheiro é gasto, fica difícil economizar ou identificar despesas desnecessárias — problema especialmente comum entre jovens adultos e trabalhadores autônomos.

---

## 💡 Proposta da solução

Uma aplicação CLI leve e direta que permite:

- registrar gastos
- categorizar despesas
- visualizar relatórios simples
- acompanhar total gasto

Ao iniciar, a aplicação também consulta a cotação atual do dólar (USD → BRL) via API externa e exibe para o usuário.

---

## 🎯 Público-alvo

Qualquer pessoa que queira controlar seus gastos de forma simples diretamente pelo terminal.

---

## ⚙️ Funcionalidades

- Exibir cotação atual do dólar (USD → BRL) ao iniciar
- Adicionar gasto com descrição, valor e categoria
- Listar todos os gastos registrados
- Filtrar gastos por categoria
- Exibir resumo com total por categoria e percentual
- Remover gasto pelo ID

---

## 🛠️ Tecnologias utilizadas

- Python 3.9+
- requests — consumo de API REST externa
- pytest — testes automatizados (unitários + integração)
- ruff — linting e análise estática
- GitHub Actions — integração contínua (CI)

---

## 🌐 API pública utilizada

| API | Endpoint | Dados |
|-----|----------|------|
| AwesomeAPI Economia | https://economia.awesomeapi.com.br/json/last/USD-BRL | Cotação atual do dólar em reais |

---

## 📦 Instalação

```bash
git clone https://github.com/Renatatxr19/Gastos-Pessoais
cd Gastos-Pessoais
git checkout entrega-intermediaria
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
