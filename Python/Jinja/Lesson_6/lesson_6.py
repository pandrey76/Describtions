# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Jinja #6. Наследование (расширение) шаблонов.
# Именованные блоки
# {% block <имя блока> %}
# {% endblock %}
# Данные блоки и используются для расширения базового шаблона нашей страницы.

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from jinja2 import Environment, FileSystemLoader


def func_1():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about.htm')

    output = template.render()
    print(output)


# Обращаемся к шаблону через относительный путь к базовому шаблону
def func_2():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_1.htm')

    output = template.render()
    print(output)


# Используем обращение, через self к блоку title
def func_3():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_2.htm')

    output = template.render()
    print(output)


# Через super обращаемся к блоку базового шаблона и взятия от туда информации
def func_4():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_3.htm')

    output = template.render()
    print(output)


# В данной функции покзываем, что если мы не обращаемся к базовому шаблону через метод super, то именованный блок в
# дочернем шаблоне полностью переписывает содержимое таково же блока базового шаблона.
def func_5():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_4.htm')

    output = template.render()
    print(output)


# Вложенные блоки
def func_6():

    subs = ["Математика", "Физика", "Информатика", "Русский"]

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_5.htm')

    output = template.render(list_table=subs)
    print(output)


subs = ["Математика", "Физика", "Информатика", "Русский"]


# Получаем информацию из базового шаблона для конкретного именовоного блока
def func_7():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_6.htm')

    output = template.render(list_table=subs)
    print(output)


# Ещё более глубокое вложение блоков
# В данном виде если мы запустим функцию, то наш список будет пустым, т.к в базовом шаблоне default_3.htm внутри
# блока item, который мы добавили переменная {{li}} уже не существует, потому что всё что находится внутри блока не
# имеет доступа к внешнему контексту, т.е. мы не можем брать переменные из внешнего контекста за пределами этого блока.
def func_8():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_7.htm')

    output = template.render(list_table=subs)
    print(output)


# Чтобы исправить эту ситуацию послу item надо будет написать scoped и весь список снова отобразится
def func_9():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_8.htm')

    output = template.render(list_table=subs)
    print(output)


# Оправдаем добавление блока item, мы его прописали для более гибкого управления шаблоном
def func_10():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about_9.htm')

    output = template.render(list_table=subs)
    print(output)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Вложенное наследование шаблонов
# Шаблоны поддерживают вложенное наследование, т.е. формирование итогового дочернего шаблона по цепочке от базового до последнего (выходного)
# ---------------------
# |    base.tpl       |              * файл base.tpl - такой же как и ex_main.htm:
# ---------------------
#         |
#        /|\
#         |
# ---------------------
# |    child1.htm     |              * файл child1.htm:  {% extends 'base.tpl' %} ...
# ---------------------
#         |
#        /|\
#         |
# ---------------------
# |    child1.htm     |               * файл child2.htm:  {% extends 'child1.htm' %} ...
# ---------------------
# Вот так по цепочке их можно расширять и получать более гибкий механизм для создания конечных страниц сайта.
# Дальнейшая обработка таких шаблонов происходит аналогичным образом как мы только что делали.
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Мы не затрагивали тему расширения базовых классов пакетов, для создания более тонкого рендеринга шаблонов или
# реализации своего собственного загрузчика.

# Официфльная документация по пакету:

# https://jinja.palletsprojects.com/en/2.11.x

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    func_1()
    func_2()
    func_3()
    func_4()
    func_5()
    func_6()
    func_7()
    func_8()
    func_9()
    func_10()
