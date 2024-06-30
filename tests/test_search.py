import pytest

from pymelon.datadict import DataDict


normal = [{"name": "John", "age": 20}, {"name": "Jane", "age": 25}]
different_keys = [
    {"name": "John", "age": 20, "email": "john@doe.com", "gpa": 3.5},
    {"name": "Jane", "age": 25, "city": "San Francisco", "height": 170},
]
with_nested_keys = [
    {
        "name": "John",
        "age": 20,
        "email": "john@doe.com",
        "university": {"name": "UofT", "location": "Toronto", "students": 1000},
    },
    {
        "name": "Jane",
        "age": 25,
        "university": {"name": "UF", "location": "Florida", "students": 2000},
    },
]

test_data = [DataDict(normal), DataDict(different_keys), DataDict(with_nested_keys)]


def test_select():
    dd = DataDict(normal)
    try:
        assert dd.select("name") == [{"name": "John"}, {"name": "Jane"}]
    except AssertionError as e:
        pytest.fail(f"failed NORMAL - select col {e}")

    try:
        assert dd.select("name", "age") == [
            {"name": "John", "age": 20},
            {"name": "Jane", "age": 25},
        ]
    except AssertionError as e:
        pytest.fail(f"failed NORMAL - select cols {e}")

    dd = DataDict(different_keys)

    try:
        assert dd.select("name", "age") == [
            {"name": "John", "age": 20},
            {"name": "Jane", "age": 25},
        ]
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS - select cols {e}")

    try:
        assert dd.select("name", "age", "email") == [
            {"name": "John", "age": 20, "email": "john@doe.com"},
            {"name": "Jane", "age": 25},
        ]
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS - select cols {e}")

    try:
        assert dd.select("city") == [{"city": "San Francisco"}]
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS - select occasional col {e}")

    dd = DataDict(with_nested_keys)

    try:
        assert dd.select("name", "age", "university.name") == [
            {"name": "John", "age": 20, "university_name": "UofT"},
            {"name": "Jane", "age": 25, "university_name": "UF"},
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS - select nested col {e}")

    try:
        assert dd.select("university.name", "university.location") == [
            {"university_name": "UofT", "university_location": "Toronto"},
            {"university_name": "UF", "university_location": "Florida"},
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS - select nested cols {e}")

    try:
        assert dd.select("name", "university") == [
            {
                "name": "John",
                "university": {"name": "UofT", "location": "Toronto", "students": 1000},
            },
            {
                "name": "Jane",
                "university": {"name": "UF", "location": "Florida", "students": 2000},
            },
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS - select dict col {e}")


def test_where():
    dd = DataDict(normal)
    try:
        assert dd.where("age", ">", 20) == [{"name": "Jane", "age": 25}]
    except AssertionError as e:
        pytest.fail(f"failed NORMAL gt - where {e}")

    try:
        assert dd.where("age", "<", 21) == [{"name": "John", "age": 20}]
    except AssertionError as e:
        pytest.fail(f"failed NORMAL lt - where {e}")

    try:
        assert dd.where("age", "==", 20) == [{"name": "John", "age": 20}]
    except AssertionError as e:
        pytest.fail(f"failed NORMAL eq - where {e}")

    try:
        assert dd.where("age", "!=", 20) == [{"name": "Jane", "age": 25}]
    except AssertionError as e:
        pytest.fail(f"failed NORMAL neq - where {e}")

    try:
        assert dd.where("age", ">=", 20) == [
            {"name": "John", "age": 20},
            {"name": "Jane", "age": 25},
        ]
    except AssertionError as e:
        pytest.fail(f"failed NORMAL gte - where {e}")

    try:
        assert dd.where("age", ">", 20) == [{"name": "Jane", "age": 25}]
    except AssertionError as e:
        pytest.fail(f"failed NORMAL gt - where {e}")

    try:
        assert dd.where("age", ">", 50) == []
    except AssertionError as e:
        pytest.fail(f"failed NORMAL lte - where {e}")

    dd = DataDict(different_keys)

    try:
        assert dd.where("gpa", ">", 3.0) == [
            {"name": "John", "age": 20, "email": "john@doe.com", "gpa": 3.5}
        ]
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS gt - where {e}")

    try:
        assert dd.where("gpa", "<", 4.0) == [
            {"name": "John", "age": 20, "email": "john@doe.com", "gpa": 3.5}
        ]
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS lt - where {e}")

    try:
        assert dd.where("height", "==", 170) == [
            {"name": "Jane", "age": 25, "city": "San Francisco", "height": 170}
        ]
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS eq - where {e}")

    try:
        assert dd.where("gpa", "!=", 3.5) == []
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS neq - where {e}")

    try:
        assert dd.where("height", ">=", 170) == [
            {"name": "Jane", "age": 25, "city": "San Francisco", "height": 170},
        ]
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS gte - where {e}")

    try:
        assert dd.where("height", "<=", 180) == [
            {"name": "Jane", "age": 25, "city": "San Francisco", "height": 170},
        ]
    except AssertionError as e:
        pytest.fail(f"failed DIFFERENT_KEYS lte - where {e}")

    dd = DataDict(with_nested_keys)

    try:
        assert dd.where("university.location", "==", "Toronto") == [
            {
                "name": "John",
                "age": 20,
                "email": "john@doe.com",
                "university": {"name": "UofT", "location": "Toronto", "students": 1000},
            },
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS eq - where {e}")

    try:
        assert dd.where("university.location", "!=", "Toronto") == [
            {
                "name": "Jane",
                "age": 25,
                "university": {"name": "UF", "location": "Florida", "students": 2000},
            },
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS neq - where {e}")

    try:
        assert dd.where("university.students", ">", 1000) == [
            {
                "name": "Jane",
                "age": 25,
                "university": {"name": "UF", "location": "Florida", "students": 2000},
            },
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS gt - where {e}")

    try:
        assert dd.where("university.students", "<", 1500) == [
            {
                "name": "John",
                "age": 20,
                "email": "john@doe.com",
                "university": {"name": "UofT", "location": "Toronto", "students": 1000},
            },
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS lt - where {e}")

    try:
        assert dd.where("university.students", ">=", 1500) == [
            {
                "name": "Jane",
                "age": 25,
                "university": {"name": "UF", "location": "Florida", "students": 2000},
            },
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS gte - where {e}")

    try:
        assert dd.where("university.students", "<=", 1000) == [
            {
                "name": "John",
                "age": 20,
                "email": "john@doe.com",
                "university": {"name": "UofT", "location": "Toronto", "students": 1000},
            },
        ]
    except AssertionError as e:
        pytest.fail(f"failed WITH_NESTED_KEYS lte - where {e}")
