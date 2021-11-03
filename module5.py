#Вывод всех нечётных элементов списка. Если таковых нет, вывести 0.

def odd_items(inputList):
    a = inputList
    b = [x for x in a if x%2]
    print('Нечётные элементы списка: ', b)
