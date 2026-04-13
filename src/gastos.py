import json
import uuid
from datetime import datetime
from pathlib import Path

ARQUIVO_DADOS = Path("dados.json")

CATEGORIAS = [
    "Alimentação",
    "Transporte",
    "Saúde",
    "Moradia",
    "Lazer",
    "Educação",
    "Roupas",
    "Outros",
]


def carregar_dados() -> list[dict]:
    if not ARQUIVO_DADOS.exists():
        return []
    with open(ARQUIVO_DADOS, encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(gastos: list[dict]) -> None:
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)


def adicionar_gasto(descricao: str, valor: float, categoria: str) -> dict:
    if not descricao or not descricao.strip():
        raise ValueError("A descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    if categoria not in CATEGORIAS:
        raise ValueError(f"Categoria inválida: {categoria}")

    gasto = {
        "id": str(uuid.uuid4())[:8],
        "descricao": descricao.strip(),
        "valor": round(valor, 2),
        "categoria": categoria,
        "data": datetime.now().strftime("%Y-%m-%d"),
    }
    gastos = carregar_dados()
    gastos.append(gasto)
    salvar_dados(gastos)
    return gasto


def listar_gastos(categoria: str | None = None) -> list[dict]:
    gastos = carregar_dados()
    if categoria:
        gastos = [g for g in gastos if g["categoria"] == categoria]
    return gastos


def remover_gasto(gasto_id: str) -> bool:
    gastos = carregar_dados()
    novos = [g for g in gastos if g["id"] != gasto_id]
    if len(novos) == len(gastos):
        return False
    salvar_dados(novos)
    return True


def resumo_por_categoria(gastos: list[dict]) -> dict[str, float]:
    resumo: dict[str, float] = {}
    for g in gastos:
        cat = g["categoria"]
        resumo[cat] = round(resumo.get(cat, 0) + g["valor"], 2)
    return resumo


def total_gastos(gastos: list[dict]) -> float:
    return round(sum(g["valor"] for g in gastos), 2)
