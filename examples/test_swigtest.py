import json

import swigtest
from pydantic import BaseModel, ConfigDict
from rich import print

from custom_json_encoder import CustomJSONEncoder

CustomJSONEncoder.on_error = "object"


def print_json(o):
    print(json.dumps(o, cls=CustomJSONEncoder, indent=2))


class PydanticModel(BaseModel):
    string_int_map: swigtest.StringIntMap
    test_class: swigtest.TestClass

    model_config = ConfigDict(arbitrary_types_allowed=True)


print("=== Vector ===")
int_vector = swigtest.createIntVector(5)
print_json(int_vector)
print()

print("=== Map ===")
string_int_map = swigtest.createStringIntMap()
print_json(string_int_map)
print()

print("=== Unordered map ===")
unordered_map = swigtest.createStringIntUnorderedMap()
print_json(unordered_map)
print()

print("=== Array ===")
int_array = swigtest.createIntArray3()
print_json(int_array)
print()

print("=== Pair ===")
pair = swigtest.createIntDoublePair(10, 20.5)
print_json(pair)
print()

print("=== Wrapped class ===")
test_class = swigtest.TestClass()
print_json(test_class)
print()

print("=== Pydantic model ===")
print_json(
    PydanticModel(
        string_int_map=swigtest.createStringIntMap(),
        test_class=swigtest.TestClass(),
    ).model_dump()
)
