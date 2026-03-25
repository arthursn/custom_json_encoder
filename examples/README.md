# SWIG C++ to Python Example

This example demonstrates how to use SWIG to wrap C++ code for use in Python, along with JSON serialization of the wrapped objects.

## Prerequisites

- CMake (3.21 or higher)
- C++ compiler with C++17 support
- Python 3 with development headers
- SWIG 4.0 or higher

## Building the Example

To build the example, run the following commands from the `examples` directory:

```bash
cmake -B build
cmake --build build
```

This will generate the Python module `_swigtest.so` (or `.pyd` on Windows) and copy the `swigtest.py` wrapper to the examples directory.

## Running the Example

After building, you can run the example with:

```bash
python test_swigtest.py
```

This will demonstrate various C++ STL containers being created in C++ and then serialized to JSON in Python using the custom JSON encoder.

## What's Included

- `swigtest.hpp`: C++ header with classes and functions to be wrapped
- `swigtest.i`: SWIG interface file
- `test_swigtest.py`: Python script that tests the wrapped code
- `CMakeLists.txt`: CMake build configuration
