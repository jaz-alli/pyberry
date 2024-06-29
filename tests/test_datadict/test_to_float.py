import pytest
import pymelon as pm

data_age_str_int = [
    {"id": 1, "name": "Alice", "age": "30"},
    {"id": 2, "name": "Bob", "age": "25"},
    {"id": 3, "name": "Charlie", "age": "35"},
    {"id": 4, "name": "David", "age": "28"},
    {"id": 5, "name": "Eve", "age": "22"},
    {"id": 6, "name": "Frank", "age": "31"},
    {"id": 7, "name": "Grace", "age": "27"},
    {"id": 8, "name": "Helen", "age": 24},
    {"id": 9, "name": "Isaac", "age": "33"},
    {"id": 10, "name": "Judy", "age": 29},
]

data_age_float = [
    {"id": 1, "name": "Alice", "age": 30.0},
    {"id": 2, "name": "Bob", "age": 25.0},
    {"id": 3, "name": "Charlie", "age": 35.0},
    {"id": 4, "name": "David", "age": 28.0},
    {"id": 5, "name": "Eve", "age": 22.0},
    {"id": 6, "name": "Frank", "age": 31.0},
    {"id": 7, "name": "Grace", "age": 27.0},
    {"id": 8, "name": "Helen", "age": 24.0},
    {"id": 9, "name": "Isaac", "age": 33.0},
    {"id": 10, "name": "Judy", "age": 29.0},
]


def test_to_float():
    dd_age_str_int = pm.DataDict(data_age_str_int)
    dd_age_float = pm.DataDict(data_age_float)

    try:
        dd_age_str_int.to_float("age")
        assert dd_age_str_int.data == dd_age_float.data

    except AssertionError as e:
        pytest.fail(f"default n value: {e}")

    try:
        pytest.raises(ValueError, dd_age_str_int.to_float, "name")
    except AssertionError as e:
        pytest.fail(f"user n value - cannot convert to float: {e}")
