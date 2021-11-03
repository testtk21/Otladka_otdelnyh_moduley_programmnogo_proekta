#Вывод всех чётных элементов списка. Если таковых нет, вывести 0.

def even_items(inputList):
    a = inputList
    b = [x for x in a if not x%2]
    print ('Чётные элементы списка: ', b )
