import pytest

@pytest.mark.database

@pytest.mark.xfail(reason="aguardando a implementação da conexão real do banco de dados.")

def test_busca_no_banco_real():

  """

  Teste de integração que valida se um gasto persistido no banco de dados

  pode ser consultado corretamente.

  """

  assert False