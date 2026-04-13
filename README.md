# Gerenciador de Gastos Pessoais

## Sobre o projeto

Controlar gastos no dia a dia é mais difícil do que parece. Sem um registro claro de onde o dinheiro vai, fica quase impossível economizar ou perceber o que está pesando no bolso — e isso afeta muita gente, especialmente jovens e autônomos. Esse projeto nasceu dessa necessidade: uma ferramenta simples, sem complicação, para quem quer ter mais consciência financeira.

## O que ele faz

- Adiciona gastos com descrição, valor e categoria
- Lista todos os gastos registrados
- Filtra por categoria
- Mostra um resumo com total por categoria e percentual
- Remove gastos pelo ID

## Para quem é

Para qualquer pessoa que queira organizar os próprios gastos de forma prática, sem precisar de aplicativo, conta ou internet.

## Tecnologias

- Python 3.9+
- `pytest` — testes automatizados
- `ruff` — análise estática do código
- GitHub Actions — integração contínua (CI)

## Como instalar

```bash
git clone https://github.com/Renatatxr19/Gastos-Pessoais
cd Gastos-Pessoais
python -m venv .venv
.venv\Scripts\activate  # Linux/Mac: source .venv/bin/activate
pip install -e ".[dev]"
```

## Como executar

```bash
python -m src.gui
```

## Rodando os testes

```bash
pytest tests/ -v
```

## Rodando o lint

```bash
ruff check src/
```

## Versão

`1.0.0`

## Autora

Renata Teixeira — renata.teixeira@sempreceub.com

## Repositório

https://github.com/Renatatxr19/Gastos-Pessoais
