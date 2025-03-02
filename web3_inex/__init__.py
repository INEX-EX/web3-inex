from eth_account import Account  # noqa: E402

from importlib.metadata import version

__version__ = version("web3")


from web3_inex.main import (
    AsyncWeb3,
    Web3,
)
from web3_inex.providers import (
    AsyncBaseProvider,
    AutoProvider,
    BaseProvider,
    JSONBaseProvider,
    PersistentConnection,
)
from web3_inex.providers.persistent import (  # noqa: E402
    AsyncIPCProvider,
    PersistentConnectionProvider,
    WebSocketProvider,
)
from web3_inex.providers.eth_tester import (  # noqa: E402
    AsyncEthereumTesterProvider,
    EthereumTesterProvider,
)
from web3_inex.providers.ipc import (  # noqa: E402
    IPCProvider,
)
from web3_inex.providers.rpc import (  # noqa: E402
    AsyncHTTPProvider,
    HTTPProvider,
)
from web3_inex.providers.legacy_websocket import (  # noqa: E402
    LegacyWebSocketProvider,
)

import web3_inex.node

__all__ = [
    "__version__",
    "Account",
    # web3:
    "AsyncWeb3",
    "Web3",
    # providers:
    "AsyncBaseProvider",
    "AsyncEthereumTesterProvider",
    "AsyncHTTPProvider",
    "AsyncIPCProvider",
    "AutoProvider",
    "BaseProvider",
    "EthereumTesterProvider",
    "HTTPProvider",
    "IPCProvider",
    "JSONBaseProvider",
    "LegacyWebSocketProvider",
    "PersistentConnection",
    "PersistentConnectionProvider",
    "WebSocketProvider",
]

