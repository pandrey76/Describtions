# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Jinja #4. Загрузчики.

# https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.Environment

# https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.FileSystemLoader

# PackageLoader - для загрузки шаблонов из пакета;
# DictLoader - для загрузки шаблонов из словаря;
# FunctionLoader - для загрузки на основе функции;
# PrefixLoader - загрузчик, использующий словарь для построения подкаталогов;
# ChoiceLoader - загрузчик, содержащий список других загрузчиков (если один не сработает, выбирается следующий);
# ModuleLoader - загрузчик для скомпилированных шаблонов.

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {"name": "Alexey", "old": 18, "weight": 78.5},
    {"name": "Nicolay", "old": 28, "weight": 82.3},
    {"name": "Ivan", "old": 33, "weight": 94.0},
]


def func_1():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('main.htm')   # Template
    msg = tm.render(users=persons)

    print(msg)


def loadTpl(path):
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные {{u}}'''


def func_2():
    file_loader = FunctionLoader(loadTpl)   # Передаём ссылку на функцию.
    env = Environment(loader=file_loader)

    tm = env.get_template('index')  # Template
    msg = tm.render(u=persons[0])

    print(msg)


def func_3():
    file_loader = FunctionLoader(loadTpl)   # Передаём ссылку на функцию.
    env = Environment(loader=file_loader)

    tm = env.get_template('index_1')  # Template
    msg = tm.render(u=persons[0])

    print(msg)


if __name__ == '__main__':
    func_1()
    func_2()
    func_3()
