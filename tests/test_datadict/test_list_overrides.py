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


def test_append():
    dd = pm.DataDict(data)

    try:
        dd.append({"id": 11, "name": "John", "age": 32})
        assert len(dd) == 11
    except AssertionError as e:
        pytest.fail(f"append dict: {e}")

    try:
        pytest.raises(TypeError, dd.append, 5)
    except AssertionError as e:
        pytest.fail(f"append non-dict: {e}")
