from queue import Queue

import pytest

from assignment1.src.producer_consumer import Consumer, Producer, run_demo


def test_all_items_transferred():
    source = ["A", "B", "C", "D"]
    result = run_demo(source)
    assert sorted(result) == sorted(source), "All items should be transferred."


def test_order_preserved():
    source = ["apple", "banana", "cherry"]
    result = run_demo(source)
    assert result == source, "Order of items should be preserved(FIFO)"


def test_empty_source():
    source = []
    result = run_demo(source)
    assert result == [], "Empty source should produce an empty destination"


def test_no_duplicates_or_missing():
    source = [str(i) for i in range(20)]
    result = run_demo(source)

    assert len(result) == len(source), "No items should be lost"
    assert sorted(result) == sorted(source), "No duplicate or missing items"


def test_multiple_runs_are_deterministic():
    """
    to ensure no state leaking between runs.
    """
    source = ["x", "y", "z"]
    assert run_demo(source) == source
    #
    assert run_demo(source) == source


def test_invalid_source_type():
    with pytest.raises(TypeError):
        run_demo("not_a_list")  # type: ignore[arg-type]


def test_source_contains_none():
    source = ["A", None, "C"]

    with pytest.raises(Exception):
        run_demo(source)


def test_poison_pill_in_middle():
    q = Queue()
    destination = []
    poison_pill = object()

    # poison pill intentionally placed inside the source
    source = ["X", "Y", poison_pill, "Z"]

    producer = Producer(q, source, poison_pill)
    consumer = Consumer(q, destination, poison_pill)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    # consumer should stop at poison pill and not consume Z
    assert destination == ["X", "Y"]


def test_immidiate_poison_pill():
    source = []
    # poison pill will be sent immidiately
    result = run_demo(source)
    assert result == []
