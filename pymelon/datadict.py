from collections import defaultdict
from typing import Any


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

    def _to_datadict(self, data: list[dict]) -> "DataDict":
        """
        Converts a list of dicts to a DataDict object.

        Args:
            data (list[dict]): A list of dicts to be converted to a DataDict object.

        Returns:
            DataDict: A DataDict object containing the list of dicts.
        """

        return DataDict(data)

    def _get_nested_value(self, record: dict, key_path: str) -> Any:
        """
        Helper method to get a nested value from a dictionary.

        Args:
            record (dict): The dictionary to search for the nested value.
            key_path (str): The path to the nested value.
            Each key in the key_path is seperated by a delimiter.
            The default delimiter is ".".

        Returns:
            Any: The nested value if found, None otherwise.
        """

        current_value = record
        for key in key_path.split("."):
            if isinstance(current_value, dict) and key in current_value:
                current_value = current_value[key]
            else:
                return None
        return current_value

    def head(self, n: int = 5) -> "DataDict":
        """
        Returns the first `n` elements of the DataDict.
        If n is greater than the number of elements in the DataDict, all elements are returned.

        Args:
            n (int): The number of elements to return from the beginning of the DataDict.

        Returns:
            list[dict]: A list containing the first `n` elements of the DataDict.
        """

        return self.data[:n]

    def tail(self, n: int = 5) -> "DataDict":
        """
        Returns the last `n` elements of the DataDict.
        If n is greater than the number of elements in the DataDict, all elements are returned.

        Args:
            n (int): The number of elements to return from the end of the DataDict.

        Returns:
            list[dict]: A list containing the last `n` elements of the DataDict.
        """

        return self.data[-n:]

    def to_int(self, key):
        """
        Converts the value of a specified key in each dictionary within the DataDict to an integer.

        Args:
            key (str): The key whose values are to be converted to integers.

        Raises:
            ValueError: If the value associated with the key cannot be converted to an integer.
        """
        for item in self.data:
            if key in item:
                try:
                    item[key] = int(item[key])
                except:
                    raise ValueError(
                        f"Encountered value '{item[key]}' of type {type(item[key])} that cannot be cast to an int."
                    )

    def to_float(self, key):
        """
        Converts the value of a specified key in each dictionary within the DataDict to an float.

        Args:
            key (str): The key whose values are to be converted to floats.

        Raises:
            ValueError: If the value associated with the key cannot be converted to a float.
        """
        for item in self.data:
            if key in item:
                try:
                    item[key] = float(item[key])
                except:
                    raise ValueError(
                        f"Encountered value '{item[key]}' of type {type(item[key])} that cannot be cast to an float."
                    )

    def to_str(self, key):
        """
        Converts the value of a specified key in each dictionary within the DataDict to an string.

        Args:
            key (str): The key whose values are to be converted to strings.

        Raises:
            ValueError: If the value associated with the key cannot be converted to a string.
        """
        for item in self.data:
            if key in item:
                try:
                    item[key] = str(item[key])
                except:
                    raise ValueError(
                        f"Encountered value '{item[key]}' of type {type(item[key])} that cannot be cast to an str."
                    )

    def select(self, *keys: str) -> "DataDict":
        """
        Selects and returns a DataDict object with the specified keys.
        The DataDict object can be treated exactly like a list of dicts,
        but can also perform more complex queries

        Args:
            *keys (str): The keys to select. This can be any number of keys found in the DataDict.
            Each additional key to select can be added as a new unnamed argument. For example:
            DataDict.select("name", "age")
            Nested keys can be accessed by using a delimiter (default is ".").
            For example: "user.name". So this query would also be valid:
            DataDict.select("name", "age", "user.name")

        Returns:
            DataDict: A DataDict object containing the selected dicts.
            The DataDict object can be treated exactly like a list of dicts, but can also perform more complex queries
        """

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

    def where(self, key: str, comparison: str, value: Any) -> "DataDict":
        """
        Filters the DataDict object based on the specified field and comparison.
        The DataDict object can be treated exactly like a list of dicts, but can also perform more complex queries.

        Args:
            key (str): The key to filter by. This can be any key found in the DataDict.
            comparison (str): The comparison operator to use. This can be any comparison operator found in the DataDict.
            value (Any): The value to compare the field to.

        Returns:
            DataDict: A DataDict object containing the filtered dicts.
            The DataDict object can be treated exactly like a list of dicts, but can also perform more complex queries.
        """

        result = []

        def get_nested_value(item: dict, key_path: str) -> Any:
            current_value = item
            for key in key_path.split("."):
                if isinstance(current_value, dict) and key in current_value:
                    current_value = current_value[key]
                else:
                    return None
            return current_value

        for item in self.data:
            key_value = get_nested_value(item, key)
            if key_value is not None:
                if comparison == "==" and key_value == value:
                    result.append(item)
                elif comparison == "!=" and key_value != value:
                    result.append(item)
                elif comparison == ">" and key_value > value:
                    result.append(item)
                elif comparison == "<" and key_value < value:
                    result.append(item)
                elif comparison == ">=" and key_value >= value:
                    result.append(item)
                elif comparison == "<=" and key_value <= value:
                    result.append(item)
        return self._to_datadict(result)

    def min(self, key) -> int | float:
        """
        Finds the minimum value for a specified key in the DataDict where the values are of type int or float.

        Args:
            key (str): The key to find the minimum value for.

        Returns:
            int | float: The minimum value found for the specified key. Returns None if no suitable value is found.

        Raises:
            ValueError: If a value under the specified key is not an int or float.
        """

        current_min = None
        for item in self.data:
            if key in item:
                try:
                    float(item[key])
                    if current_min == None:
                        current_min = item[key]
                    else:
                        current_min = min(item[key], current_min)

                except:
                    raise ValueError(
                        f"Encountered type {type(item[key])}. The min function can only be used with int or float types."
                    )
        return current_min

    def max(
        self, key: str | int | float | tuple[str | int | float, ...]
    ) -> int | float:
        """
        Finds the maximum value for a specified key in the DataDict where the values are of type int or float.

        Args:
            key (str): The key to find the maximum value for.

        Returns:
            int | float: The maximum value found for the specified key.
        """

        current_max = None
        for item in self.data:
            if key in item:

                try:
                    if not isinstance(item[key], int):
                        float(item[key])
                    if current_max == None:
                        current_max = item[key]
                    else:
                        current_max = max(item[key], current_max)

                except:
                    raise ValueError(
                        f"Encountered type {type(item[key])}. The min function can only be used with ints or floats."
                    )
        return current_max

    def _get_numerical_field_values(
        self, key: str | int | float | tuple[str | int | float, ...]
    ) -> list[int | float]:
        values = []
        for item in self.data:
            if key in item:
                try:
                    if not isinstance(item[key], int):
                        float(item[key])
                    values.append(item[key])
                except:
                    raise ValueError(
                        f"Encountered type {type(item[key])}. The min function can only be used with ints or floats."
                    )
        return values

    def _calculate_mean(self, values: list[int | float]) -> int | float:
        return sum(values) / len(values)

    def mean(
        self, key: str | int | float | tuple[str | int | float, ...]
    ) -> int | float:
        """
        Calculates the mean value for a specified key in the DataDict where the values are of type int or float.

        Args:
            key (str): The key to find the mean value for.

        Returns:
            int | float: The mean value found for the specified key.
        """

        values = self._get_numerical_field_values(key)
        return self._calculate_mean(values)

    def _calculate_median(self, values: list[int | float]) -> int | float:
        values.sort()
        if len(values) % 2 == 0:
            return (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2
        else:
            return values[len(values) // 2]

    def median(
        self, key: str | int | float | tuple[str | int | float, ...]
    ) -> int | float:
        """
        Calculates the median value for a specified key in the DataDict where the values are of type int or float.

        Args:
            key (str): The key to find the median value for.

        Returns:
            int | float: The median value found for the specified key.
        """

        values = self._get_numerical_field_values(key)
        return self._calculate_median(values)

    def append(self, item: dict):
        """
        Overrides the append method to ensure only dictionaries can be added to the DataDict.

        Args:
            item (dict): The dictionary to be appended to the DataDict.

        Raises:
            TypeError: If the item is not a dictionary.
        """

        if not isinstance(item, dict):
            raise TypeError("Only dictionaries can be appended to DataDict")
        # super().append(item)
        self.data.append(item)

    def __len__(self):
        return len(self.data)
