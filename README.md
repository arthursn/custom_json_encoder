# custom-json-encoder

A Python module that extends `json.JSONEncoder` to serialize objects not natively supported by JSON.

## Features

- Handles SWIG-wrapped C++ objects and containers
- Supports NumPy arrays and Pandas DataFrames/Series
- Configurable floating-point precision and error handling

## Usage

```python
import json
import numpy as np
import pandas as pd
from custom_json_encoder import CustomJSONEncoder

# Optional configuration
CustomJSONEncoder.float_num_sig_fig = 3
CustomJSONEncoder.on_error = "object"

# Example data
data = {
    "numpy_array": np.array([1.2345, 2.3456, 3.4567]),
    "pandas_series": pd.Series([4.5678, 5.6789]),
    "nested": {
        "float_value": 6.7890123
    }
}

# Serialize
json_string = json.dumps(data, cls=CustomJSONEncoder, indent=2)
print(json_string)
```

Output:
```json
{
  "numpy_array": [1.23, 2.35, 3.46],
  "pandas_series": [4.57, 5.68],
  "nested": {
    "float_value": 6.79
  }
}
```

## Examples

Check out the `examples` directory for a complete example showing how to use the custom JSON encoder with SWIG-wrapped C++ objects. The example demonstrates serializing various C++ STL containers and custom classes.
