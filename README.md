# 💰 Gerenciador de Gastos Pessoais
[![CI Workflow](https://github.com/Renatatxr19/Gastos-Pessoais/actions/workflows/ci.yml/badge.svg)](https://github.com/Renatatxr19/Gastos-Pessoais/actions)

---

## 🔗 Deploy

* **Aplicação publicada através do PyPI (Python Package Index)**
* **Link para visualização web:** [pypi.org/project/gastos-pessoais-cli](https://pypi.org/project/gastos-pessoais-cli)

### 📥 Instalação e Atualização

* Para instalar a biblioteca ou garantir que você está utilizando a versão mais recente com todas as correções de caminhos, execute o comando abaixo no seu terminal:
  ```bash
  pip install --upgrade gastos-pessoais-cli

### 🚀 Como Executar
1. Após a instalação, você pode iniciar a aplicação de qualquer diretório do seu terminal apenas digitando:
    ```bash
    gastos

**💡 Nota sobre o PATH (Caso o comando não seja encontrado):**
Se o Windows emitir um alerta dizendo que o comando gastos não foi reconhecido, significa que a pasta de scripts do Python não está nas variáveis de ambiente do seu sistema.

2. Você pode executar o CLI especificando o caminho completo do executável padrão do usuário:
    ```bash
    %APPDATA%\Python\Python314\Scripts\gastos.exe

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

## 🧪 Suíte de Testes Automatizados

A aplicação conta com uma cobertura completa de testes automatizados utilizando o `pytest`, totalizando **25 cenários mapeados**:

1. **Testes de Unidade**
2. **Testes de Integração da API**
3. **Testes de Integração do Banco de Dados**

---

## 🚀 Integração Contínua (GitHub Actions)

A pipeline automatizada foi configurada para validar cada commit enviado ao repositório de forma independente.

---

## Integrantes do grupo

- Renata Teixeira de Jesus
- Pedro Silveira Newlands Machado


