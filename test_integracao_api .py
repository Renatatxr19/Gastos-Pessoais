"""
Testes de integração — valida a comunicação com a API de cotação (AwesomeAPI).

Estratégia dupla:
  - test_cotacao_retorna_float_real: faz requisição REAL à API (marcado com
    pytest.mark.integration para poder ser pulado em ambientes sem rede).
  - test_cotacao_com_mock: usa monkeypatch para simular a resposta da API,
    garantindo que o fluxo de dados não quebre a aplicação mesmo offline.
"""

import pytest
import requests

from src.app import obter_cotacao_dolar


# ---------------------------------------------------------------------------
# Teste de integração real (requer internet)
# ---------------------------------------------------------------------------

@pytest.mark.integration
def test_cotacao_retorna_float_real():
    """Chama a API de verdade e verifica que o retorno é um float positivo."""
    cotacao = obter_cotacao_dolar()
    assert cotacao is not None, (
        "A API retornou None — verifique a conexão ou o endpoint."
    )
    assert isinstance(cotacao, float), (
        f"Esperado float, recebeu {type(cotacao)}"
    )
    assert cotacao > 0, "A cotação deve ser maior que zero."


# ---------------------------------------------------------------------------
# Testes com mock (não requerem internet — rodam sempre no CI)
# ---------------------------------------------------------------------------

class FakeResponse:
    """Simula um objeto requests.Response bem-sucedido."""

    def raise_for_status(self):
        pass  # sem erro HTTP

    def json(self):
        return {"USDBRL": {"bid": "5.25"}}


class FakeResponseHTTPError:
    """Simula um requests.Response que lança HTTPError."""

    def raise_for_status(self):
        raise requests.exceptions.HTTPError("404 Not Found")

    def json(self):
        return {}


def test_cotacao_mock_retorna_float(monkeypatch):
    """Com resposta mockada, obter_cotacao_dolar deve retornar float correto."""
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: FakeResponse())
    cotacao = obter_cotacao_dolar()
    assert cotacao == 5.25
    assert isinstance(cotacao, float)


def test_cotacao_mock_timeout_retorna_none(monkeypatch):
    """Quando a API demorar demais, a função deve retornar None sem explodir."""
    def fake_get(*args, **kwargs):
        raise requests.exceptions.Timeout

    monkeypatch.setattr(requests, "get", fake_get)
    cotacao = obter_cotacao_dolar()
    assert cotacao is None


def test_cotacao_mock_connection_error_retorna_none(monkeypatch):
    """Sem conexão, a função deve retornar None sem explodir."""
    def fake_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError

    monkeypatch.setattr(requests, "get", fake_get)
    cotacao = obter_cotacao_dolar()
    assert cotacao is None


def test_cotacao_mock_http_error_retorna_none(monkeypatch):
    """Quando a API retornar status de erro (ex: 500), deve retornar None."""
    monkeypatch.setattr(
        requests, "get", lambda *args, **kwargs: FakeResponseHTTPError()
    )
    cotacao = obter_cotacao_dolar()
    assert cotacao is None


def test_cotacao_mock_chave_ausente_retorna_none(monkeypatch):
    """Se a estrutura do JSON mudar e faltar a chave, deve retornar None."""
    class FakeResponseChaveErrada:
        def raise_for_status(self):
            pass

        def json(self):
            return {"outra_chave": {}}

    monkeypatch.setattr(
        requests, "get", lambda *args, **kwargs: FakeResponseChaveErrada()
    )
    cotacao = obter_cotacao_dolar()
    assert cotacao is None
