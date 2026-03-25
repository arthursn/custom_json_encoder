#include <array>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>

// Class definitions
class TestClass {
public:
    std::map<std::string, double> MyDoubleMap;
    std::array<int, 3> MyArray;
    std::array<int, 5> UnserializableArray;

    TestClass()
    {
        MyDoubleMap["one"] = 1.0;
        MyDoubleMap["two"] = 2.0;
        MyDoubleMap["pi"] = 3.14;

        MyArray[0] = 42;
        MyArray[1] = 69;
        MyArray[2] = 420;
    }
};

std::vector<int> createIntVector(int size)
{
    std::vector<int> vec;
    for (int i = 0; i < size; i++) {
        vec.push_back(i);
    }
    return vec;
}

std::map<std::string, int> createStringIntMap()
{
    std::map<std::string, int> map;
    map["one"] = 1;
    map["two"] = 2;
    map["three"] = 3;
    return map;
}

std::unordered_map<std::string, int> createStringIntUnorderedMap()
{
    std::unordered_map<std::string, int> map;
    map["one"] = 1;
    map["two"] = 2;
    map["three"] = 3;
    return map;
}

std::array<int, 3> createIntArray3()
{
    std::array<int, 3> arr = { 1, 2, 3 };
    return arr;
}

std::pair<int, double> createIntDoublePair(int i, double d)
{
    return std::make_pair(i, d);
}
