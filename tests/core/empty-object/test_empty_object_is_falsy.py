from web3_inex._utils.empty import (
    empty,
)


def test_empty_object_is_falsy():
    assert bool(empty) is False
    assert not empty
