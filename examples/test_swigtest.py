import json

import swigtest
from pydantic import BaseModel, ConfigDict
from rich import print

from custom_json_encoder import CustomJSONEncoder

CustomJSONEncoder.on_error = "object"


def json_dumps(o):
    return json.dumps(o, cls=CustomJSONEncoder, indent=4)


class PydanticModel(BaseModel):
    string_int_map: swigtest.StringIntMap
    test_class: swigtest.TestClass
    model_config = ConfigDict(arbitrary_types_allowed=True)


print("=== Testing vector ===")
int_vector = swigtest.createIntVector(5)
print(json_dumps(int_vector))
print()

print("=== Testing map ===")
string_int_map = swigtest.createStringIntMap()
print(json_dumps(string_int_map))
print()

print("=== Testing unordered_map ===")
unordered_map = swigtest.createStringIntUnorderedMap()
print(json_dumps(unordered_map))
print()

print("=== Testing array ===")
int_array = swigtest.createIntArray3()
print(json_dumps(int_array))
print()

print("=== Testing pair ===")
pair = swigtest.createIntDoublePair(10, 20.5)
print(json_dumps(pair))
print()

print("=== Testing regular class ===")
test_class = swigtest.TestClass()
print(json_dumps(test_class))
print()

print("=== Testing pydantic model ===")
print(
    json_dumps(
        PydanticModel(
            string_int_map=swigtest.createStringIntMap(),
            test_class=swigtest.TestClass(),
        ).model_dump()
    )
)
