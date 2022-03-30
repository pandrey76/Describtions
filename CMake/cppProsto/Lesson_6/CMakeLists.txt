cmake_minimum_required (VERSION 3.5)

# https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html

project(package_find)

# Здесь мы дополнительно указываем дополнительные пути для поиска к модулям или к нужным скриптам
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/modules
                      ${CMAKE_MODULE_PATH})

# устанавливаем глобальную строковую переменную и она будет доступна во всех модулях.
set(all_found_result "ok")

# some actions
# Включаем модуль, в нашем случае: ${CMAKE_SOURCE_DIR}/cmake/modules/test.cmake
include(test)

# find package by own script
# Поиск OpenSSl (Установлен ли OpenSSL, установлен ли OpenSSL для разработчика, заголовочные файлы и т.д.), для этого
# CMake использует свои собственные скрипты:https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html
# здесь представлен список всех имеющихся скриптов уже встроенных в CMake для поиска стандартных модулей.
# Если в этом списке отсутствуют необходимые пакеты, то скрипт поиска придётся писать самому.
# Для стандартного поиска в команду find_package надо передавать имя без предиката "Find". Например: FindMFC надо
# передать просто MFC.
find_package(_OpenSSL)

# Add an executable
add_executable(package_find main.cpp)

# Это кастыль, здесь после того как отработали все скрипты cmake мы сравниваем значение нашей глобальной переменной
# и если она равна "ok", то значит все библиотеки корректно найдены.
if(all_found_result STREQUAL "ok")
  message("all libraries was found")
else()
  # Когда мы выводим сообщение с "FATAL_ERROR", то генерация прекращается.
  message( FATAL_ERROR "${all_found_result}. Not all libraries was found!" )
endif()

# Сообщения
# Ссылка на документацию: https://cmake.org/cmake/help/v3.0/command/message.html
message( STATUS         " status " )
message( WARNING        " warning " )
message( AUTHOR_WARNING " author warning " )
# Процесс продолжается, но процесс генерации прекращается
message( SEND_ERROR     " send error " )
# Если какие-нибудь вещи устарели, например поиск и ро факту старые библиотеки можно выдать статус DEPRICATION
message( DEPRECATION    " deprecation " )
# Фатальная ошибка, процесс генерации прекращается
message( FATAL_ERROR    " fatal error " )
