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


def test_mean():
    dd = pm.DataDict(data)

    try:
        assert dd.mean("age") == 28.4
    except AssertionError as e:
        pytest.fail(f"int column: {e}")

    try:
        pytest.raises(ValueError, dd.mean, "name")
    except AssertionError as e:
        pytest.fail(f"values are not numerical: {e}")


def test_median():
    dd = pm.DataDict(data)

    try:
        assert dd.median("age") == 28.5
    except AssertionError as e:
        pytest.fail(f"int column: {e}")

    try:
        pytest.raises(ValueError, dd.median, "name")
    except AssertionError as e:
        pytest.fail(f"values are not numerical: {e}")


def test_max():
    dd = pm.DataDict(data)

    try:
        assert dd.max("age") == 35
    except AssertionError as e:
        pytest.fail(f"int column: {e}")

    try:
        pytest.raises(ValueError, dd.max, "name")
    except AssertionError as e:
        pytest.fail(f"values are not numerical: {e}")


def test_min():
    dd = pm.DataDict(data)

    try:
        assert dd.min("age") == 22
    except AssertionError as e:
        pytest.fail(f"int column: {e}")

    try:
        pytest.raises(ValueError, dd.min, "name")
    except AssertionError as e:
        pytest.fail(f"values are not numerical: {e}")
