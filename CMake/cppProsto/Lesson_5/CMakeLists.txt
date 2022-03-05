cmake_minimum_required(VERSION 3.5)

project (main)


# Add sub directories
# сначала собираем независимые проекты
# add_subdirectory говорит cmake что добавляется директория, точнее подпроект в котором
# должен быть в наличии файл CMakeLists.txt
add_subdirectory(sub_project1)
add_subdirectory(sub_project2)
# основной проект самый последний, т.е происходит сборка имено его, Потому что нужно
# чтобы создался первый проект потом второй, а потом самый основной.
add_subdirectory(main)