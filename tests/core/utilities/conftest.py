import pytest

from web3_inex.main import (
    Web3,
)
from web3_inex.providers.eth_tester import (
    EthereumTesterProvider,
)


@pytest.fixture(scope="module")
def w3():
    provider = EthereumTesterProvider()
    return Web3(provider)
