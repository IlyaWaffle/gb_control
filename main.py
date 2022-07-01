print('Контрольная работа GB: написать программу, которая из имеюшегося массива строк создает'
      '\nновый массив из строк, длина которых больше или равна 3')
input("Нажмите 'Enter' для продолжения")
print("Вводите слова/цифры/числа через пробел ")
list = [input() for i in range(5)]
print("Текущий массив: ")
print(list)
index = 0


def array_sorting(array):
    global index
    for i in array:
        if len(i) <= 3:
            index += 1


array_sorting(list)
second_array = [0 for i in range(index)]


def create_new_array(array):
    index = 0
    for i in list:
        if len(i) <= 3:
            array[index] = i
            index += 1
    print(array)

print('\nПереформированный массив: ')
create_new_array(second_array)