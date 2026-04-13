from src.gastos import (
    CATEGORIAS,
    adicionar_gasto,
    listar_gastos,
    remover_gasto,
    resumo_por_categoria,
    total_gastos,
)

LINHA = "-" * 42


def cabecalho():
    print("\n" + "=" * 42)
    print("   💰  GERENCIADOR DE GASTOS PESSOAIS")
    print("=" * 42)


def menu_principal():
    print(f"\n{LINHA}")
    print("  1. Adicionar gasto")
    print("  2. Listar todos os gastos")
    print("  3. Listar por categoria")
    print("  4. Resumo por categoria")
    print("  5. Remover gasto")
    print("  0. Sair")
    print(LINHA)
    return input("  Escolha uma opção: ").strip()


def escolher_categoria() -> str:
    print("\nCategorias disponíveis:")
    for i, cat in enumerate(CATEGORIAS, 1):
        print(f"  {i}. {cat}")
    while True:
        escolha = input("  Número da categoria: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(CATEGORIAS):
            return CATEGORIAS[int(escolha) - 1]
        print("  Opção inválida. Tente novamente.")


def exibir_gastos(gastos: list[dict]):
    if not gastos:
        print("\n  Nenhum gasto encontrado.")
        return
    print(f"\n{'ID':^8} {'Data':^12} {'Categoria':^14} {'Descrição':^18} {'Valor':>8}")
    print(LINHA + "-" * 14)
    for g in gastos:
        print(
            f"  {g['id']:<6} {g['data']:<12} {g['categoria']:<14} "
            f"{g['descricao'][:16]:<18} R$ {g['valor']:>7.2f}"
        )
    print(LINHA + "-" * 14)
    print(f"  Total: R$ {total_gastos(gastos):.2f}")


def fluxo_adicionar():
    print(f"\n{LINHA}")
    print("  NOVO GASTO")
    descricao = input("  Descrição: ").strip()
    if not descricao:
        print("  Descrição não pode ser vazia.")
        return
    valor_str = input("  Valor (R$): ").strip().replace(",", ".")
    try:
        valor = float(valor_str)
    except ValueError:
        print("  Valor inválido.")
        return
    categoria = escolher_categoria()
    try:
        gasto = adicionar_gasto(descricao, valor, categoria)
        print(f"\n  Gasto adicionado com sucesso! ID: {gasto['id']}")
    except ValueError as e:
        print(f"\n  Erro: {e}")


def fluxo_listar():
    gastos = listar_gastos()
    print(f"\n{LINHA}")
    print("  TODOS OS GASTOS")
    exibir_gastos(gastos)


def fluxo_listar_categoria():
    categoria = escolher_categoria()
    gastos = listar_gastos(categoria)
    print(f"\n{LINHA}")
    print(f"  GASTOS — {categoria.upper()}")
    exibir_gastos(gastos)


def fluxo_resumo():
    gastos = listar_gastos()
    if not gastos:
        print("\n  Nenhum gasto registrado.")
        return
    resumo = resumo_por_categoria(gastos)
    total = total_gastos(gastos)
    print(f"\n{LINHA}")
    print("  RESUMO POR CATEGORIA")
    print(LINHA)
    for cat, val in sorted(resumo.items(), key=lambda x: -x[1]):
        pct = (val / total * 100) if total else 0
        barra = "█" * int(pct / 5)
        print(f"  {cat:<14} R$ {val:>8.2f}  {barra} {pct:.0f}%")
    print(LINHA)
    print(f"  TOTAL GERAL:   R$ {total:.2f}")


def fluxo_remover():
    gastos = listar_gastos()
    exibir_gastos(gastos)
    if not gastos:
        return
    gasto_id = input("\n  ID do gasto a remover: ").strip()
    if remover_gasto(gasto_id):
        print("  Gasto removido com sucesso.")
    else:
        print("  ID não encontrado.")


def main():
    cabecalho()
    acoes = {
        "1": fluxo_adicionar,
        "2": fluxo_listar,
        "3": fluxo_listar_categoria,
        "4": fluxo_resumo,
        "5": fluxo_remover,
    }
    while True:
        opcao = menu_principal()
        if opcao == "0":
            print("\n  Até logo!\n")
            break
        elif opcao in acoes:
            acoes[opcao]()
        else:
            print("  Opção inválida.")


if __name__ == "__main__":
    main()
