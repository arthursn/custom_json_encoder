cmake_minimum_required(VERSION 3.21)

project(swigtest VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)

# Find Python
find_package(
  Python3
  COMPONENTS Interpreter Development
  REQUIRED)
include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${Python3_INCLUDE_DIRS})

# Find SWIG
find_package(SWIG REQUIRED)
include(UseSWIG)

# Set SWIG properties
set_source_files_properties(swigtest.i PROPERTIES CPLUSPLUS ON SWIG_MODULE_NAME
                                                               swigtest)

# Create SWIG module
swig_add_library(
  swigtest
  LANGUAGE python
  SOURCES swigtest.i)

# Link against Python
target_link_libraries(swigtest ${Python3_LIBRARIES})

# Set output properties
execute_process(
  COMMAND "${Python3_EXECUTABLE}" -c
          "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))"
  OUTPUT_VARIABLE EXT_SUFFIX
  OUTPUT_STRIP_TRAILING_WHITESPACE)

set_target_properties(
  swigtest PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
                      SUFFIX "${EXT_SUFFIX}")

# Copy the Python wrapper to the output directory
add_custom_command(
  TARGET swigtest
  POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_BINARY_DIR}/swigtest.py
          "${CMAKE_CURRENT_SOURCE_DIR}")
