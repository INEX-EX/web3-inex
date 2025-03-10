import pytest

from eth_utils import (
    is_same_address,
)

from web3_inex._utils.events import (
    get_event_data,
)


@pytest.mark.parametrize(
    "contract_fn,event_name,call_args,expected_args",
    (
        ("logNoArgs", "LogAnonymous", [], {}),
        ("logNoArgs", "LogNoArguments", [], {}),
        ("logSingle", "LogSingleArg", [12345], {"arg0": 12345}),
        ("logSingle", "LogSingleWithIndex", [12345], {"arg0": 12345}),
        ("logSingle", "LogSingleAnonymous", [12345], {"arg0": 12345}),
        ("logDouble", "LogDoubleArg", [12345, 54321], {"arg0": 12345, "arg1": 54321}),
        (
            "logDouble",
            "LogDoubleAnonymous",
            [12345, 54321],
            {"arg0": 12345, "arg1": 54321},
        ),
        (
            "logDouble",
            "LogDoubleWithIndex",
            [12345, 54321],
            {"arg0": 12345, "arg1": 54321},
        ),
        (
            "logTriple",
            "LogTripleArg",
            [12345, 54321, 98765],
            {"arg0": 12345, "arg1": 54321, "arg2": 98765},
        ),
        (
            "logTriple",
            "LogTripleWithIndex",
            [12345, 54321, 98765],
            {"arg0": 12345, "arg1": 54321, "arg2": 98765},
        ),
        (
            "logQuadruple",
            "LogQuadrupleArg",
            [12345, 54321, 98765, 56789],
            {"arg0": 12345, "arg1": 54321, "arg2": 98765, "arg3": 56789},
        ),
        (
            "logQuadruple",
            "LogQuadrupleWithIndex",
            [12345, 54321, 98765, 56789],
            {"arg0": 12345, "arg1": 54321, "arg2": 98765, "arg3": 56789},
        ),
    ),
)
def test_event_data_extraction(
    w3,
    emitter,
    wait_for_transaction,
    emitter_contract_log_topics,
    emitter_contract_event_ids,
    contract_fn,
    event_name,
    call_args,
    expected_args,
):
    function = getattr(emitter.functions, contract_fn)
    event_id = getattr(emitter_contract_event_ids, event_name)
    txn_hash = function(event_id, *call_args).transact()
    txn_receipt = wait_for_transaction(w3, txn_hash)

    assert len(txn_receipt["logs"]) == 1
    log_entry = txn_receipt["logs"][0]

    event_abi = emitter.get_event_by_name(event_name).abi

    event_topic = getattr(emitter_contract_log_topics, event_name)
    is_anonymous = event_abi["anonymous"]

    if is_anonymous:
        assert event_topic not in log_entry["topics"]
    else:
        assert event_topic in log_entry["topics"]

    event_data = get_event_data(w3.codec, event_abi, log_entry)

    assert event_data["args"] == expected_args
    assert event_data["blockHash"] == txn_receipt["blockHash"]
    assert event_data["blockNumber"] == txn_receipt["blockNumber"]
    assert event_data["transactionIndex"] == txn_receipt["transactionIndex"]
    assert is_same_address(event_data["address"], emitter.address)
    assert event_data["event"] == event_name


def test_dynamic_length_argument_extraction(
    w3,
    emitter,
    wait_for_transaction,
    emitter_contract_log_topics,
    emitter_contract_event_ids,
):
    string_0 = "this-is-the-first-string-which-exceeds-32-bytes-in-length"
    string_1 = "this-is-the-second-string-which-exceeds-32-bytes-in-length"
    txn_hash = emitter.functions.logDynamicArgs(string_0, string_1).transact()
    txn_receipt = wait_for_transaction(w3, txn_hash)

    assert len(txn_receipt["logs"]) == 1
    log_entry = txn_receipt["logs"][0]

    event_abi = emitter.get_event_by_name("LogDynamicArgs").abi

    event_topic = emitter_contract_log_topics.LogDynamicArgs
    assert event_topic in log_entry["topics"]

    string_0_topic = w3.keccak(text=string_0)
    assert string_0_topic in log_entry["topics"]

    event_data = get_event_data(w3.codec, event_abi, log_entry)

    expected_args = {
        "arg0": string_0_topic,
        "arg1": string_1,
    }

    assert event_data["args"] == expected_args
    assert event_data["blockHash"] == txn_receipt["blockHash"]
    assert event_data["blockNumber"] == txn_receipt["blockNumber"]
    assert event_data["transactionIndex"] == txn_receipt["transactionIndex"]
    assert is_same_address(event_data["address"], emitter.address)
    assert event_data["event"] == "LogDynamicArgs"
