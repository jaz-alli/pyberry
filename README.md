# pyberry

## DataDict Class

*Detailed docs to come shortly.


### `DataDict.select(*keys)`
Selects specified keys from the data dictionary. If a key does not exist in all records, it will be omitted from those records.

**Parameters:**
- **`*keys` (Any):** The keys to select. This can be any number of keys in the DataDict.

**Returns:**
- `DataDict`: A DataDict containing only the selected keys.

### `DataDict.where(key: str, comparison: str, value: Any)`
Filters the DataDict object based on the specified field and comparison.
The DataDict object can be treated exactly like a list of dicts, but can also perform more complex queries.

**Parameters:**
- **`key` (Any):** The key to filter by. This can be any key found in the DataDict.
- comparison (str): The comparison operator to use. This can be any comparison operator found in the DataDict.
- value (Any): The value to compare the field to.

**Returns:**  
- `Datadict`: A DataDict object containing the filtered dicts.

### `DataDict.to_float(key: Any)`
Converts the values of the specified key to floats. If conversion is not possible, raises a `ValueError`.\
Modifies the DataDict in place.

**Parameters:**
- **`key` (Any):** The key whose values are to be converted to float.\
Modifies the DataDict in place.

### `DataDict.to_str(key: Any)`
Converts the values of the specified key to strings.\
Modifies the DataDict in place.

**Parameters:**
- **`key` (Any):** The key whose values are to be converted to string.

### `DataDict.median(key: Any)`
Calculates the median of the numerical values in the specified key. If the key contains non-numeric values, raises a `ValueError`.

**Parameters:**
- **`key` (Any):** The key for which the median is to be calculated.

**Returns:**
- `int | float`: The median of the key values.

### `DataDict.mean(key: Any)`
Calculates the mean of the numerical values in the specified key. If the key contains non-numeric values, raises a `ValueError`.

**Parameters:**
- **`key` (Any):** The key for which the mean is to be calculated.

**Returns:**
- `int | float`: The mean of the key values.

### `DataDict.max(key: Any)`
Calculates the maximum value out of all numerical values in the specified key. If the key contains non-numeric values, raises a `ValueError`.

**Parameters:**
- **`key` (Any):** The key for which the maximum value is to be calculated.

**Returns:**
- `int | float`: The maximum value of the key values.

### `DataDict.min(key: Any)`
Calculates the minimum value out of all numerical values in the specified key. If the key contains non-numeric values, raises a `ValueError`.

**Parameters:**
- **`key` (Any):** The key for which the minimum value is to be calculated.

**Returns:**
- `int | float`: The minimum value of the key values.

### `DataDict.tail(n: int = 5)`
Returns the last `n` elements of the data dictionary.

**Parameters:**
- **`n` (int):** An integer specifying the number of elements to return from the end of the data dictionary (default is 5).

**Returns:**
- `DataDict`: A DataDict representing the last `n` elements.

### `DataDict.head(n: int = 5)`
Returns the first `n` elements of the data dictionary.

**Parameters:**
- **`n` (int):** An integer specifying the number of elements to return from the end of the data dictionary (default is 5).

**Returns:**
- `DataDict`: A DataDict representing the first `n` elements.