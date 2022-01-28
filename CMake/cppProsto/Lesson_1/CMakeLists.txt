# Минимальная версия CMake
cmake_minimum_required(VERSION 2.6)

# Название проекта
project(cmake_example_1)
# Теперь вместо имени проекта можно использовать макрос ${PROJECT_NAME}

# Если не определять тип сборки, то по умолчанию Release
# Тип сборки можно передать через командную строку (cmake _DCMAKE ...)
set(CMAKE_BUILD_TYPE Debug)
#set(CMAKE_BUILD_TYPE Release)

# set(CMAKE_CXX_STANDARD 11)    # enable C++11 standard
# set(CMAKE_CXX_STANDARD 14)    # enable C++14 standard
# set(CMAKE_CXX_STANDARD 17)    # enable C++17 standard
# or
# set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++98")
# set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++03")
# set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
# set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
# set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")
# Самая последняя версия стандарта
set (CMAKE_CXX_FLAG "${CMAKE_CXX_FLAGS} -std=c++1y")

# Если в проекте присутствуют файлы *.с, то для их компиляции настраиваем флаги компиляторя C
# set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c89")
# set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c90")
# set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99")
set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11")

# включаем все предупреждения компилятора (02 - уровень оптимизации)
#add definitions( =Wall -02)
# or
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

# Создаем переменную SOURCE и добавляем в неё все исходные файлы
#set(SOURCES main.cpp)
# or
file(GLOB
            CPPS "*.cpp")
# Собираем в один список все файлы по регулярному выражению
# В нашем случае в переменную CPPS добавляются все файлы по шаблону *.cpp
# То есть из директории, где лежит наш файл CMakeLists.txt будут найдены все файлы с
# с расширением cpp. Хидеры добавлять не надо, объектные файлы генерятся на основе cpp файлов.

# Создаём исполняемый файл
# add_executable(${PROJECT_NAME} main.cpp)
# add_executable(${PROJECT_NAME} ${SOURCES})
# or
add_executable(${PROJECT_NAME} ${CPPS})

# Генерация makefile
# Переходим в папку с файлом CMakeLists.txt и запускаем команду
# admin1@ubuntu18:~/work/Education/Describtions/CMake/cppProsto/Lesson_1$ cmake .
# При этом создаётся куча мусора в директории с исходными файлами
# Поэтому автор предлагает создать папку build там где лежит CMakeLists.txt,
# перейти в неё и запустить генерацию Makefile от туда
# admin1@ubuntu18:~/work/Education/Describtions/CMake/cppProsto/Lesson_1/build$ cmake ..

# Далее запускаем утилиту make
