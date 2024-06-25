food = ['apple', 'coconut', 'banana']
print(food[0])
food[1] = 'peach'
print(food)  # хранят не сами элементы а хранят ссылки на элементы
food.append(True)  # элементы могут хранить разные значения
print(food)  # append добавляет значение в конец списка
# food.extend('string')  # вывел каждый символ по отдельности
# print(food)
food.extend(['string', 2])  # он принимает последовательность
print(food)
food.remove('apple')
print(food)
# проверяем есть ли элемент в нашем списке
print('coconut' in food)
# проверяем отсутствие элемента в нашем списке
print('coconut' not in food)
print(food[0:2:2])