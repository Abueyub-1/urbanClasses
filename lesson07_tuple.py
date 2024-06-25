# кортеж не изменяется как лист
tuple_ = 1, 2, 3, 4  # кортеж без круглых скобок
tuple_2 = (1, 2, 3, 4)  # кортеж с круглыми скобками
tuple_3 = tuple([1, 2, 3, 4, 'Hello'])
print(type(tuple_))
print(tuple_2)
print(tuple_3)
# неизменяемость упорядоченность элементы разные занимают мало места в памяти
print(tuple_[0])
# при изменении элементов внутри кортежа выйдет ошибка
# Кортежи подходят для хранения данных, которые не должны быть изменены (например, координаты, дата, константы)
# занимают мало места в памяти
print(tuple_2.__sizeof__())
print(tuple_3.__sizeof__())
# сам кортеж не изменяем хотя внутри он может содержать изменяемые объекты
tuple_4 = ([1, 2], 0)
print(tuple_4)
# изменяю элементы списка в кортеже
tuple_4[0][0] = 2
# обращаемся по порядковому номеру [0]
# достаю элемент с индексом [0]
# меняю на = 2
print(tuple_4)
# он хранит ссылки на объекты мы изменяем не сам кортеж а ее содержимое
tuple_4 = ([1, 2], 0) + (1, 2)  # Можно сделать канкотенацию
# Два исключения:
print(tuple_4)
tuple_4 = ([1, 2], 0) * 3  # Можно сделать умножение
print(tuple_4)
