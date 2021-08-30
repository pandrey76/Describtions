# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Jinja #5. Конструкции include, import.

# Конструкция include
# Как правило страницу сайта делят на три части. На заголовок, сам контент и подвал страницы
# -----------------------------
# |  header                   |
# -----------------------------
# |  content                  |
# -----------------------------
# |  footer                   |
# -----------------------------
# Заголовок (header) и подвал (footer) страницы как правило не меняются и чтобы не дублировать эту информацию
# её можно отдельно подключить и наполнить конкретную страницу конкретным контентом, т.е исходный шаблон
# страницы мы можем разделить на три части и каждую часть поместить в свой отдельный файл и потом их соединить
# с помощью конструкции include.

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from jinja2 import Environment, FileSystemLoader


def func_1():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('page.htm')
    msg = tm.render()

    print(msg)


# Формирование страницы из тех шаблонов, которые он смог найти
def func_2():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('page_with_no_raising_except_template_missing.htm')
    msg = tm.render()

    print(msg)


def func_3():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('page_1.htm')
    msg = tm.render(domain='http://proproprogs.ru', title="Про Jinja")

    print(msg)


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Если в блоке include надо подключить несколько страниц, то мы их и вписывем

# {% include['page1.htm', 'page2.htm'] ignore missing %}

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Конструкция import
# Отличия конструкции import от конструкции include состоит в том, что при импорте файл не добавляется, но мы можем
# использовать функционал этого файла. Например можно импортировать макрос.

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def func_4():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('page_2.htm')
    msg = tm.render(domain='http://proproprogs.ru', title="Про Jinja")

    print(msg)


def func_5():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('page_3.htm')
    msg = tm.render(domain='http://proproprogs.ru', title="Про Jinja")

    print(msg)


def func_6():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('page_4.htm')
    msg = tm.render(domain='http://proproprogs.ru', title="Про Jinja")

    print(msg)


if __name__ == '__main__':
    func_1()
    func_2()
    func_3()
    func_4()
    func_5()
    func_6()
