# Основные парадигмы ООП
# * Инкапсуляция;
# * Наследование;
# * Полиморфизм.

class PointTmp:
    """
        Класс для предоставления координат точек на плоскоси
    """
    pass


print(PointTmp.__doc__)


class Point:
    """
        Класс для предоставления координат точек на плоскоси
    """

    x = 1
    y = 1


print(Point.__doc__)
print(Point.__name__)   # Point
print(dir(Point))   # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                    # '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
                    # '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
                    # '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x', 'y']

pt = Point()
# Переменная __dict__ содержит коллекцию из локальных переменных
print(pt.__dict__)  # Вернётся пустой список, ротому, что локальных переменных пока нет.
                    # {}
Point.x = 100
print(pt.x, pt.y)  # 100 1
# Похоже на поведение статических переменных, как в языках Java и C++
print(id(pt), id(Point), sep="\n")  # 139807776168816
                                    # 32298248
pt.x = 5
pt.y = 10
print(pt.x, Point.x)  # 5 100

print(pt.__dict__)  # {'x': 5, 'y': 10}


# В терминологии ООП языка Python переменные x и y внутри класса Point
# или его экземпляров называется аттрибутами или свойтвами.
# С аттрибутами класса или его экземплярами можно рпботать через следующик функции:

#    * getattr(obj, name [, default])    - возвращает значение аттрибута;
#    * hasattr(obj, name)                - проверяет на наличие аттрибута name в object;
#    * setattr(obj, name, value)         - задаёт значение аттрибута (если аттрибут не существует, то он создаётся);
#    * delattr(obj, name)                - удаляет аттрибут с именем name.

print(getattr(pt, 'x'))  # 5
# print(getattr(pt, 'z'))   # Будет сгенерированно исключение типа AttributeError
print(getattr(pt, 'z', False))   # False

print(hasattr(pt, 'z'))  # False
print(hasattr(pt, 'y'))  # True

setattr(pt, 'z', 7)
print(pt.__dict__)  #{'x': 5, 'y': 10, 'z': 7}

delattr(pt, 'z')
print(pt.__dict__)  #{'x': 5, 'y': 10}

# Тоже самое, только с классом
setattr(Point, 'z', 7)
print(dir(Point))   # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                    # '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
                    # '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
                    # '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x', 'y', 'z']

Point.description = "Some class"
print(dir(Point))   # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                    # '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
                    # '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
                    # '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'description', 'x', 'y', 'z']

# Можно и таким образом работать с аттрибутами, но фунции предоставляют большую гибкость
pt.msg = "hello"
print(pt.__dict__)  # {'x': 5, 'y': 10, 'msg': 'hello'}

# pt.sss  # Будет сгенерировано исключение типа "AttributeError: 'Point' object has no attribute 'sss'"

# Но если мы будем обращатся через функцию getattr и укажем третий аргумент False, то исключение не будет
res = getattr(pt, "sss", False)
print(res)  # False

# Кроме того существуют функции hasattr и delattr, которые имеют определённую логику.

# Удалить аттрибут можно ещё с помощью оператора del
del pt.x
print(pt.__dict__)  # {'y': 10, 'msg': 'hello'}

# Функция isinstance позволяет проверить является ли объект экземпляром класса, таким образом мы можем
# проверять принадлежность того или иного экземпляра определённому классу.
print(isinstance(pt, Point))  # True


class Point3D:
    pass


print(isinstance(pt, Point3D))  # False

# Задание для самоподготовки
#    Объявить класс Point3D для точек с тремя координатами x, y, z. Создайте несколько экземпляров
# этого класса и через них выведети в консоль значения x, y, z. Далее, сделайте следующие манипуляции:
#        * поменяйте любое значение координаты в классе Point3D и посмотрите как это повлияет на
#                                                                    отображение величины экземпляров классов;
#        * удалите координату z в классе Point3D и убедитесь, что она будет отсутствовать во всех экземплярах;
#        * поменяйте координату в каком-либо экземпляре класса и посмотрите нп результат.

