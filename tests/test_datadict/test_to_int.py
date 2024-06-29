import pytest
import pymelon as pm

data_age_str = [
    {"id": 1, "name": "Alice", "age": "30"},
    {"id": 2, "name": "Bob", "age": "25"},
    {"id": 3, "name": "Charlie", "age": "35"},
    {"id": 4, "name": "David", "age": "28"},
    {"id": 5, "name": "Eve", "age": "22"},
    {"id": 6, "name": "Frank", "age": "31"},
    {"id": 7, "name": "Grace", "age": "27"},
    {"id": 8, "name": "Helen", "age": "24"},
    {"id": 9, "name": "Isaac", "age": "33"},
    {"id": 10, "name": "Judy", "age": "29"},
]

data_age_num = [
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


def test_to_int():
    dd_age_str = pm.DataDict(data_age_str)
    dd_age_num = pm.DataDict(data_age_num)

    try:
        dd_age_str.to_int("age")
        assert dd_age_str.data == dd_age_num.data

    except AssertionError as e:
        pytest.fail(f"default n value: {e}")

    try:
        pytest.raises(ValueError, dd_age_str.to_int, "name")
    except AssertionError as e:
        pytest.fail(f"user n value - cannot convert to int: {e}")
