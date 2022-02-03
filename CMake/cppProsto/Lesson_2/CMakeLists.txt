cmake_minimum_required(VERSION 3.5)

project (cmake_example_2)

# Устанавливаем версию нашей программы
set (cmake_example_2_VERSION_MAJOR 0)
set (cmake_example_2_VERSION_MINOR 9)
set (cmake_example_2_VERSION_PATCH 3)
set (cmake_example_2_VERSION_TWEAK 4)
set (cmake_example_2_VERSION "${cmake_example_2_VERSION_MAJOR}.${cmake_example_2_VERSION_MINOR}.${cmake_example_2_VERSION_PATCH}.${cmake_example_2_VERSION_TWEAK}")

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall")

file(GLOB
            CPP_SOURCES "src/*.cpp")

#  Генерим файлы
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
configure_file(
                "${PROJECT_SOURCE_DIR}/include/ver.h.in"
                "${PROJECT_BINARY_DIR}/version.h"
              )

configure_file(
                "${PROJECT_SOURCE_DIR}/include/path.h.in"
                "${PROJECT_BINARY_DIR}/path.h"
              )

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

include_directories("${PROJECT_SOURCE_DIR}/include")
# аналогичную операцию можно провести и через установку флагов компилятора
# -I "../include/" через set (CMAKE_CXX_FLAGS ...
# но это не удобно, т.к. строка с установкой флагов компилятора будет расти.

include_directories("${PROJECT_BINARY_DIR}")

add_executable(${PROJECT_NAME} ${CPP_SOURCES})
