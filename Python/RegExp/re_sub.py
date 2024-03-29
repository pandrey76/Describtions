
# https://pythonz.net/references/named/re.sub/

# Возвращает новую строку, полученную в результате замены по указанному шаблону.
#
#     re.sub(pattern, repl, string, count=0, flags=0) -> str
#
#     pattern:    Шаблон(строка или объект pattern), вхождение которого в строку, нужно заменить.
#     repl:       Строка, которую требуется поставить вместо прежней, или функция, которая производит замену.В строке
#                 поддерживаются обращения к группам символов, определённым в шаблоне.
#     string:     Строка, для которой нужно произвести замену по шаблону.
#     count = 0:  Максимальное количество замен, которое дозволено произвести.Положительное целое.Если не указано(0), то
#                 будут произведены все возможные замены.
#     3.1
#     flags = 0:  Флаги управления интерпретацией регулярного выражения. Если соответствие шаблону в строке не найдено,
#                 то вернётся неизменённая строка. На заметку Если в repl указана строка, то символы с экранированием
#                 будут обработаны автоматически: например,  "\n" будет заменена на символ новой строки, "\r" на символ
#                 возврата каретки и т.п.Начиная с
#     3.6 употребление неизвестных экранирований ASCII - букв зарезервировано на будущее, а потому рассматривается как
#         ошибка(с 3.7 это также относится к pattern).При этом экранирование прочих символов, например, \ &,
#         допускается.

def test_1():
    import re

    re.sub(r'два', r'три', 'шёл дождь и два студента')
    # 'шёл дождь и три студента'

# Обратные ссылки при обработке заменяются соответствующими подстроками.Например, "\6" будет заменено подстрокой из
# группы 6, определённой в шаблоне. На заметку В некоторых случаях ссылка вида \num может быть неоднозначной
# (например, вполне может оказаться, что в 0\20 имелась ввиду группа 2, а не 20 ).Тогда желательно ссылаться на группу
# при помощи \g < num >.При помощи \g < name > можно также ссылаться на именованные группы типа(?P < name > ...).


def test_2():
    import re

    re.sub(r'([a-z]+)( .+)', r'\2 \1', 'python язык программирования')
    # ' язык программирования python'
    # \2 — это группа символов ( .+)
    # \1 — это группа символов ([a-z]+)

    re.sub(r'(?P<lang>[a-z]+)(?P<more> .+)', r'\g<more> \g<lang>', 'python язык программирования')
    # ' язык программирования python'
    re.sub(r'([a-z]+)( .+)', r'\g<2> \g<1>', 'python язык программирования')
    # ' язык программирования python'

# На заметку Начиная с 3.5 ненайденные группы заменяются пустой строкой.Начиная с 3.7 «пустые» найденные строки
# заменяются когда стоят рядом с непустыми: sub('x*', '-', 'abxd') возвращает '-a-b--d-'. В случае использования
# функции, она будет вызвана для каждой находки.Функция должна принимать один аргумент — объект находки —,
# а возвращать строку для замены.

import re


def replacer(match):
    return 'снег'


re.sub(r'дождь', replacer, 'шёл дождь и два студента')  # 'шёл снег и два студента'
