def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [1, 5, 9, 8, 7, 4, 3, 11]
target_value = 1
result_index = linear_search(my_list, target_value)

if result_index != -1:
    print(f"Значение {target_value} найдено в индексе {result_index}.")
else:
    print(f"Значение {target_value} не найдено.")

"""
def linear_search_while(arr, target):
    
    Линейный поиск с использованием цикла while.
   
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1


def linear_search_index(arr, target):
    
    Линейный поиск с использованием встроенной функции index().
    
    try:
        return arr.index(target)
    except ValueError:
        return -1

def linear_search_list_comprehension(arr, target):
    
    Линейный поиск с использованием генератора списков.
    
    indices = [i for i, item in enumerate(arr) if item == target]
    return indices[0] if indices else -1


"""