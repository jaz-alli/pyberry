from collections import defaultdict
from typing import Any


class Pyplup(list):
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
