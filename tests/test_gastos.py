import pytest

from src.gastos import (
    adicionar_gasto,
    listar_gastos,
    remover_gasto,
    resumo_por_categoria,
    total_gastos,
)


@pytest.fixture(autouse=True)
def limpar_dados(tmp_path, monkeypatch):
    arquivo = tmp_path / "dados.json"
    import src.gastos as mod
    monkeypatch.setattr(mod, "ARQUIVO_DADOS", arquivo)


class TestAdicionarGasto:
    def test_adiciona_gasto_valido(self):
        gasto = adicionar_gasto("Almoço", 25.50, "Alimentação")
        assert gasto["descricao"] == "Almoço"
        assert gasto["valor"] == 25.50
        assert gasto["categoria"] == "Alimentação"
        assert "id" in gasto
        assert "data" in gasto

    def test_valor_negativo_levanta_erro(self):
        with pytest.raises(ValueError, match="maior que zero"):
            adicionar_gasto("Teste", -10.0, "Outros")

    def test_valor_zero_levanta_erro(self):
        with pytest.raises(ValueError, match="maior que zero"):
            adicionar_gasto("Teste", 0, "Outros")

    def test_descricao_vazia_levanta_erro(self):
        with pytest.raises(ValueError, match="vazia"):
            adicionar_gasto("", 10.0, "Outros")

    def test_descricao_apenas_espacos_levanta_erro(self):
        with pytest.raises(ValueError, match="vazia"):
            adicionar_gasto("   ", 10.0, "Outros")

    def test_categoria_invalida_levanta_erro(self):
        with pytest.raises(ValueError, match="Categoria inválida"):
            adicionar_gasto("Teste", 10.0, "CategoriaFalsa")

    def test_descricao_tem_espacos_removidos(self):
        gasto = adicionar_gasto("  Uber  ", 15.0, "Transporte")
        assert gasto["descricao"] == "Uber"


class TestListarGastos:
    def test_lista_vazia_sem_dados(self):
        assert listar_gastos() == []

    def test_lista_todos_os_gastos(self):
        adicionar_gasto("Café", 5.0, "Alimentação")
        adicionar_gasto("Ônibus", 4.0, "Transporte")
        gastos = listar_gastos()
        assert len(gastos) == 2

    def test_filtra_por_categoria(self):
        adicionar_gasto("Pizza", 40.0, "Alimentação")
        adicionar_gasto("Táxi", 20.0, "Transporte")
        adicionar_gasto("Hambúrguer", 30.0, "Alimentação")
        gastos = listar_gastos("Alimentação")
        assert len(gastos) == 2
        assert all(g["categoria"] == "Alimentação" for g in gastos)

    def test_filtro_categoria_inexistente_retorna_vazio(self):
        adicionar_gasto("Café", 5.0, "Alimentação")
        gastos = listar_gastos("Saúde")
        assert gastos == []


class TestRemoverGasto:
    def test_remove_gasto_existente(self):
        gasto = adicionar_gasto("Cinema", 30.0, "Lazer")
        resultado = remover_gasto(gasto["id"])
        assert resultado is True
        assert listar_gastos() == []

    def test_remove_id_inexistente_retorna_false(self):
        resultado = remover_gasto("id-que-nao-existe")
        assert resultado is False

    def test_remove_apenas_gasto_correto(self):
        g1 = adicionar_gasto("Almoço", 20.0, "Alimentação")
        adicionar_gasto("Jantar", 35.0, "Alimentação")
        remover_gasto(g1["id"])
        gastos = listar_gastos()
        assert len(gastos) == 1
        assert gastos[0]["descricao"] == "Jantar"


class TestResumoETotal:
    def test_total_correto(self):
        adicionar_gasto("Item A", 10.0, "Outros")
        adicionar_gasto("Item B", 20.0, "Outros")
        gastos = listar_gastos()
        assert total_gastos(gastos) == 30.0

    def test_total_lista_vazia(self):
        assert total_gastos([]) == 0.0

    def test_resumo_por_categoria(self):
        adicionar_gasto("Pão", 5.0, "Alimentação")
        adicionar_gasto("Arroz", 10.0, "Alimentação")
        adicionar_gasto("Ônibus", 4.0, "Transporte")
        gastos = listar_gastos()
        resumo = resumo_por_categoria(gastos)
        assert resumo["Alimentação"] == 15.0
        assert resumo["Transporte"] == 4.0

    def test_resumo_lista_vazia(self):
        assert resumo_por_categoria([]) == {}
