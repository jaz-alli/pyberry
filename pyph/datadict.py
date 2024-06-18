from collections import defaultdict
from typing import Any

# PYBERRY


class DataDict(list):
    def __init__(self, data) -> None:
        super().__init__(data)

        self.data = data
        self.keys, self.all_types = self._get_keys_and_types()

    def _get_keys_and_types(self) -> tuple[list, dict[Any, list]]:
        """
        Extracts and returns the keys and their corresponding types from a list of dicts.

        This method processes a list of dicts, extracting each dict's keys as keys and
        the types of their corresponding values. It ensures that all entries in the list are dicts
        and aggregates the types of values associated with each key across all dicts.

        Returns:
            tuple[list, dict[Any, list]]: A tuple containing:
                - A list of unique key names found across all dicts.
                - A dict mapping each key to a list of unique types of values associated with that key.
        """

        if not isinstance(self.data, list):
            raise ValueError(f"Input should be a list - got: {type(self.data)}")

        keys = []
        all_types = defaultdict(list)

        for item in self.data:
            if not isinstance(item, dict):
                raise ValueError(
                    f"Input should be a list of dicts - got: {type(item)} in list"
                )

            for key in item.keys():
                if key not in keys:
                    keys.append(key)

                if type(item[key]) not in all_types[key]:
                    all_types[key].append(type(item[key]))

        return keys, dict(all_types)

    def _to_datadict(self, data):
        """
        Converts a list of dicts to a DataDict object.

        Args:
            data (list[dict]): A list of dicts to be converted to a DataDict object.

        Returns:
            DataDict: A DataDict object containing the list of dicts.
        """

        return DataDict(data)

    def _get_nested_value(self, record, key_path):

        current_value = record
        for key in key_path.split("."):
            if isinstance(current_value, dict) and key in current_value:
                current_value = current_value[key]
            else:
                return None
        return current_value

    def select(self, *keys):
        result = []

        for item in self.data:
            selected_item = {}
            for key in keys:
                nested_value = self._get_nested_value(item, key)
                if nested_value is not None:
                    key = key.replace(".", "_")
                    selected_item[key] = nested_value
            if selected_item:
                result.append(selected_item)
        return self._to_datadict(result)

    def where(self, field, comparison, value):
        result = []

        def get_nested_value(item, field_path):
            current_value = item
            for key in field_path.split("."):
                if isinstance(current_value, dict) and key in current_value:
                    current_value = current_value[key]
                else:
                    return None
            return current_value

        for item in self.data:
            field_value = get_nested_value(item, field)
            if field_value is not None:
                if comparison == "==" and field_value == value:
                    result.append(item)
                elif comparison == ">" and field_value > value:
                    result.append(item)
                elif comparison == "<" and field_value < value:
                    result.append(item)
                elif comparison == ">=" and field_value >= value:
                    result.append(item)
                elif comparison == "<=" and field_value <= value:
                    result.append(item)
        return self._to_datadict(result)
