#Вывод всех чётных элементов списка. Если таковых нет, вывести 0.

def even_items(inputList):
    return print('Чётные элементы списка: ', [x for x in inputList if x % 2 == 0])
        
