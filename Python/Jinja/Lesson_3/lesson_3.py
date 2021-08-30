from jinja2 import Template


# //////////////////////////////////////////////////////////////////
# Jinja #3. Фильтры и макросы: macro, call

# Весь список предопределённых фильтров Jinja
# http://jinja.palletsprojects.com/en/2.11.x/templates/
# abs(), attr(), batch(), capitalize(), center(), default(), dictsort(), escape(),
# filesizeformat(), first(), float(), forceescape(), format(), groupby(), indent(),
# int(), join(), last(), length(), list(), lower(), map(), max(), min(), pprint(),
# random(), reject(), rejectattr(), replace(), reverse(), round(), safe(), delect(),
# selectattr(), slice(), sort(), string(), striptags(), sum(), title(), tojson(),
# trim(), truncate(), unique(), upper(), urlencode(), urlize(), wordcount(), wordwrap(),
# xmlattr().

# //////////////////////////////////////////////////////////////////

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Scoda', 'price': 17300},
    {'model': 'Volvo', 'price': 44300},
    {'model': 'Lada', 'price': 21300},
]


def func_0():
    # sum - вычисление суммы поле коллекции.
    # sum(iterable, attribute=None, start=0)
    # iterable - итерируемый объект, но мы его используем в самом шаблоне.
    #   start - начальное значение, которое суммируется к общей сумме.

    # Используем дополнительный фильтр sum и производим суммирование по аттрибуту price
    # и это приводит к изменению поведения шаблона.
    tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
    tm = Template(tpl)
    msg = tm.render(cs=cars)

    print(msg)


def func_1():
    digs = [1, 2, 3, 4, 5]
    tpl = "Суммарная величина {{ cs | sum }}"
    tm = Template(tpl)
    msg = tm.render(cs=digs)

    print(msg)


def func_2():
    tpl = "Максимальная цена атомобилей {{ cs | max(attribute='price') }}"
    tm = Template(tpl)
    msg = tm.render(cs=cars)

    print(msg)


def func_3():
    tpl = "Максимальная цена атомобилей {{ (cs | max(attribute='price')).model }}"
    tm = Template(tpl)
    msg = tm.render(cs=cars)

    print(msg)


def func_4():
    tpl = "Минимальная цена атомобилей {{  cs | min(attribute='price') }}"
    tm = Template(tpl)
    msg = tm.render(cs=cars)

    print(msg)


def func_5():
    tpl = "Атомобиль {{  cs | random }}"
    tm = Template(tpl)
    msg = tm.render(cs=cars)

    print(msg)


def func_6():
    tpl = "Атомобиль {{  cs | replace('o', 'O') }}"
    tm = Template(tpl)
    msg = tm.render(cs=cars)

    print(msg)

# //////////////////////////////////////////////////////////////////

# Блок filter
# {{% filter <название фильтр> %}
# <фрагмент для применения фильтра>
# {% endfilter %}

# //////////////////////////////////////////////////////////////////


persons = [
    {"name": "Alexey", "old": 18, "weight": 78.5},
    {"name": "Nikolay", "old": 28, "weight": 82.5},
    {"name": "Ivan", "old": 33, "weight": 94.5}
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''


def func_7():
    tpl = '''
    {%- for u in users -%}
    {% filter upper %}{{u.name}}{% endfilter %}
    {% endfor -%}
    '''
    tm = Template(tpl)
    msg = tm.render(users=persons)

    print(msg)


def func_8():
    tpl = '''
    {%- for u in users -%}
    {% filter lower %}{{u.name}}{% endfilter %}
    {% endfor -%}
    '''

    tm = Template(tpl)
    msg = tm.render(users=persons)

    print(msg)


# //////////////////////////////////////////////////////////////////

# Макроопределения

# DRY - Don't Repeat Yourself (Не повторяйся)

# //////////////////////////////////////////////////////////////////
# К значению value применяется дополнительно флаг экранирования.
html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''


def func_9():

    tm = Template(html)
    msg = tm.render(users=persons)

    print(msg)

# //////////////////////////////////////////////////////////////////

# Вложенные макросы -call
# {% call[параметры]<вызов макроса> %}
# <вложенный шаблон>
# {% endcall %}


html_1 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}}
{%- endfor %}
</ul>    
{%- endmacro %}

{{list_users(users)}}
'''


def func_10():

    tm = Template(html_1)
    msg = tm.render(users=persons)

    print(msg)

# //////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////
# Формируем вложенные спистки

html_2 = ''' 
{% macro list_users(list_of_user) -%}
<ul>
{% for u in users -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
        <li>age: {{user.age}}
        <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''


# Когда мы используем caller, то вместо него подставляется ровно то, что у нас указано внутри блока call и таким
# образом у нас формируются вложенные макросы, формируеся связь блока call с каким-нибудь макросом.
def func_11():

    tm = Template(html_2)
    msg = tm.render(users=persons)

    print(msg)

# //////////////////////////////////////////////////////////////////


if __name__ == '__main__':
    func_0()
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
    func_11()
