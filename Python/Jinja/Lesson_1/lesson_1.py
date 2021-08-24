from jinja2 import Template


def func_0():
    name = "Fedor"

    # Использование f строк
    msg2 = f"Hello {name}"
    tm = Template("Hello {{ name }}.")

    msg = tm.render(name=name)
    print(msg, msg2, sep="\n")


def func_1():
    name = "Peter"
    tm = Template("Hello {{ name }}.")
    msg = tm.render(name=name)
    print(msg)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Jinja #1. Что такое конструкция {{}}
#   pip install  Jinja
# {name: Fedor}
# * {%%} - спецификатор шаблона;
# * {{ }} - выражение для вставки конструкции Python в шаблон;
# * {##} - блок комментариев;
# * # ## - строковые комментарий.

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def func_2():
    name = "Alex"
    age = 28
    tm = Template("Мне {{ a }} лет и зовут {{ n }}.")
    msg = tm.render(n=name, a=age)
    print(msg)


def func_3():
    name = "Alex"
    age = 28
    tm = Template("Мне {{ a*2 }} лет и зовут {{ n.upper() }}.")
    msg = tm.render(n=name, a=age)
    print(msg)


def func_4():
    class Person:

        def __init__(self, name, age):
            self.name = name
            self.age = age

    per = Person("Evgeniy", 33)
    tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}.")
    msg = tm.render(p=per)
    print(msg)


def func_5():
    class Person:

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def getName(self):
            return self.name

        def getAge(self):
            return self.age

    per = Person("Sergey", 20)
    tm = Template("Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}.")
    msg = tm.render(p=per)
    print(msg)


def func_6():

    per = {'name': 'Mikel', 'age': 34}
    tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}.")
    msg = tm.render(p=per)
    print(msg)


def func_7():

    per = {'name': 'Mikel', 'age': 37}
    tm = Template("Мне {{ p['age'] }} лет и зовут {{ p['name'] }}.")
    msg = tm.render(p=per)
    print(msg)


if __name__ == '__main__':
    func_0()
    func_1()
    func_2()
    func_3()
    func_4()
    func_5()
# Передача данных в шаблон с использованием словаря
    func_6()
    func_7()
