import pytest
import pymelon as pm

data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35},
    {"id": 4, "name": "David", "age": 28},
    {"id": 5, "name": "Eve", "age": 22},
    {"id": 6, "name": "Frank", "age": 31},
    {"id": 7, "name": "Grace", "age": 27},
    {"id": 8, "name": "Helen", "age": 24},
    {"id": 9, "name": "Isaac", "age": 33},
    {"id": 10, "name": "Judy", "age": 29},
]


def mighty_assert(condition, error_message):
    try:
        assert condition
    except AssertionError as e:
        pytest.fail(f"{error_message}: {e}")


def test_head():
    dd = pm.DataDict(data)
    try:
        assert dd.head() == data[:5]
    except AssertionError as e:
        pytest.fail(f"default n value: {e}")
    try:
        assert dd.head(3) == data[:3]
    except AssertionError as e:
        pytest.fail(f"user n value - less than data length: {e}")
    try:
        assert dd.head(30) == data
    except AssertionError as e:
        pytest.fail(f"user n value - greater than data length: {e}")
    try:
        pytest.raises(TypeError, dd.head, "hello")
    except AssertionError as e:
        pytest.fail(f"user n value - not an int: {e}")
