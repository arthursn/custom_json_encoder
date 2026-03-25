%module swigtest

%{
#include "swigtest.hpp"
%}

// STL containers
%include "std_array.i"
%include "std_map.i"
%include "std_pair.i"
%include "std_string.i"
%include "std_unordered_map.i"
%include "std_vector.i"

// Template instantiations
%template(IntVector) std::vector<int>;
%template(DoubleVector) std::vector<double>;
%template(StringVector) std::vector<std::string>;

%template(StringIntMap) std::map<std::string, int>;
%template(StringDoubleMap) std::map<std::string, double>;
%template(IntStringMap) std::map<int, std::string>;

%template(StringIntUnorderedMap) std::unordered_map<std::string, int>;

%template(IntArray3) std::array<int, 3>;
%template(DoubleArray5) std::array<double, 5>;

%template(IntDoublePair) std::pair<int, double>;
%template(StringIntPair) std::pair<std::string, int>;

// Nested containers
%template(VectorOfIntVector) std::vector<std::vector<int>>;
%template(MapOfVectors) std::map<std::string, std::vector<double>>;

%include "swigtest.hpp"
