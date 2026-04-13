# Gerenciador de Gastos Pessoais

![CI](https://github.com/Renatatxr19/Gastos-Pessoais)

## Descrição do problema

Muitas pessoas perdem o controle dos próprios gastos por falta de um registro simples e acessível. Sem visibilidade sobre onde o dinheiro é gasto, fica difícil economizar ou identificar despesas desnecessárias — problema especialmente comum entre jovens adultos e trabalhadores autônomos.

## Proposta da solução

Uma aplicação CLI leve e direta que permite registrar, categorizar e visualizar gastos pessoais, com resumo por categoria e total acumulado. Sem necessidade de internet, conta ou aplicativo externo.

## Público-alvo

Qualquer pessoa que queira controlar seus gastos de forma simples, diretamente pelo terminal.

## Funcionalidades

- Adicionar gasto com descrição, valor e categoria
- Listar todos os gastos registrados
- Filtrar gastos por categoria
- Ver resumo visual com total por categoria e percentual
- Remover um gasto pelo ID

## Tecnologias utilizadas

- Python 3.9+
- `pytest` — testes automatizados
- `ruff` — linting e análise estática
- GitHub Actions — integração contínua (CI)

## Instalação

```bash
git clone https:https://github.com/Renatatxr19/Gastos-Pessoais
cd gastos-pessoais
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Execução

```bash
python -m src.app
```

Exemplo de sessão:

```
==========================================
   💰  GERENCIADOR DE GASTOS PESSOAIS
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
```

## Rodando os testes

```bash
pytest tests/ -v
```

## Rodando o lint

```bash
ruff check src/
```

## Versão atual

`1.0.0`

## Autor

Renata Teixeira - renata.teixeira@sempreceub.com

## Repositório

https://github.com/Renatatxr19/Gastos-Pessoais
