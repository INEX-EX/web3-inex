from web3_inex.manager import (
    RequestManager,
)
from web3_inex.middleware import (
    AttributeDictMiddleware,
    BufferedGasEstimateMiddleware,
    ENSNameToAddressMiddleware,
    GasPriceStrategyMiddleware,
    ValidationMiddleware,
)


def test_default_sync_middleware(w3):
    expected_middleware = [
        (GasPriceStrategyMiddleware, "gas_price_strategy"),
        (ENSNameToAddressMiddleware, "ens_name_to_address"),
        (AttributeDictMiddleware, "attrdict"),
        (ValidationMiddleware, "validation"),
        (BufferedGasEstimateMiddleware, "gas_estimate"),
    ]

    default_middleware = RequestManager.get_default_middleware()

    assert default_middleware == expected_middleware
