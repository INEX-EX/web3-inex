from web3_inex._utils.method_formatters import (
    PYTHONIC_REQUEST_FORMATTERS,
    PYTHONIC_RESULT_FORMATTERS,
)
from web3_inex.middleware.formatting import (
    FormattingMiddlewareBuilder,
)

PythonicMiddleware = FormattingMiddlewareBuilder.build(
    request_formatters=PYTHONIC_REQUEST_FORMATTERS,
    result_formatters=PYTHONIC_RESULT_FORMATTERS,
)
