from jinja2 import Template


# Различные способы экранирования данных в строках


def func_0():
    data = '''Модуль Jinja вместо определения {{ name }} подставляет соответствующее значение'''

    tm = Template(data)
    msg = tm.render(name='Fedor')
    print(msg)


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Jinja #2. Экранирование. Блоки raw, for и if.
#  {% raw %} ... {% endraw %}

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def func_1():
    data = '''{% raw %}Модуль Jinja вместо определения {{ name }} подставляет соответствующее значение{% endraw %}'''

    tm = Template(data)
    msg = tm.render(name='Fedor')
    print(msg)


link = '''В HTML-документе ссылки определяются так: <a href="#">Ссылка</a>'''


def func_2():
    tm = Template(link)
    msg = tm.render()
    print(msg)
    # Данный текст в браузере отобразится как ссылка:
    # В HTML - документе ссылки определяются так: Ссылка


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Экранирование символов

# <a href="#">Ссылка</a> --> В HTML - документе ссылки определяются так: Ссылка

# e - escape (экранирование), экранирование специальных символов, которые браузер воспринимает как тэги.

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def func_3():
    tm = Template("{{ link | e }}")
    msg = tm.render(link=link)
    print(msg)


from jinja2 import escape


# Более короткая запись и данный способ более быстрее работает
def func_4():
    msg = escape(link)
    print(msg)


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Выражение for

# {% for <выражение> -%}
#   <повторяемый фрагмент>
# {% endfor %}

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 5, 'city': 'Tver'},
          {'id': 7, 'city': 'Minsk'},
          {'id': 8, 'city': 'Smolensk'},
          {'id': 11, 'city': 'Kaluga'}]

param1 = '''<select name="cities">
{% for c in cities %}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>'''


def func_5():
    tm = Template(param1)
    msg = tm.render(cities=cities)
    print(msg)


# Без переноса строки
param2 = '''<select name="cities">{% for c in cities %}<option value="{{c['id']}}">{{c['city']}}</option>{% endfor %}
</select>'''


def func_6():
    tm = Template(param2)
    msg = tm.render(cities=cities)
    print(msg)


# Добавляя знак "-" перед знаком "%" мы убираем лишние символы переноса строки и символы табуляции при этом перенос
# строки берётся из переноса сделанногог в самом шаблоне
param3 = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>'''


def func_7():
    tm = Template(param3)
    msg = tm.render(cities=cities)
    print(msg)


# Удираем лишний символ ререноса строки в конце добавив дополнительный символ "-" перед символом "%" в endfor
param4 = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''


def func_8():
    tm = Template(param4)
    msg = tm.render(cities=cities)
    print(msg)


# Убираем лишний символ переноса строки в начале добавив дополнительный символ "-" после символа "%"
param5 = '''<select name="cities">
{%- for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''


def func_9():
    tm = Template(param5)
    msg = tm.render(cities=cities)
    print(msg)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Выражение if

# {% if <условие> %}
#   <фрагмент при истинности условия>
# {% endfor %}

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


param6 = '''<select name="cities">
{%- for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endif -%}    
{% endfor -%}
</select>'''


def func_10():
    tm = Template(param6)
    msg = tm.render(cities=cities)
    print(msg)


param7 = '''<select name="cities">
{%- for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% else -%}    
    {{c['city']}}
{% endif -%}    
{% endfor -%}
</select>'''


def func_11():
    tm = Template(param7)
    msg = tm.render(cities=cities)
    print(msg)


param7 = '''<select name="cities">
{%- for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% else -%}    
    {{c['city']}}
{% endif -%}    
{% endfor -%}
</select>'''


def func_11():
    tm = Template(param7)
    msg = tm.render(cities=cities)
    print(msg)


param7 = '''<select name="cities">
{%- for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% else -%}    
    {{c['city']}}
{% endif -%}    
{% endfor -%}
</select>'''


def func_11():
    tm = Template(param7)
    msg = tm.render(cities=cities)
    print(msg)


param8 = '''<select name="cities">
{%- for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "Moscow" -%}    
    <option>{{c['city']}}</option>
{% else -%}    
    {{c['city']}}
{% endif -%}    
{% endfor -%}
</select>'''


def func_12():
    tm = Template(param8)
    msg = tm.render(cities=cities)
    print(msg)


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
    func_12()
