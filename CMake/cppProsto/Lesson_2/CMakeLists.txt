cmake_minimum_required(VERSION 3.5)

project (cmake_example_2)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall")

file(GLOB
            CPP_SOURCES "src/*.cpp")

include_directories("${PROJECT_SOURCE_DIR}/include")
# аналогичную операцию можно провести и через установку флагов компилятора
# -I "../include/" через set (CMAKE_CXX_FLAGS ...
# но это не удобно, т.к. строка с установкой флагов компилятора будет расти.

add_executable(${PROJECT_NAME} ${CPP_SOURCES})
