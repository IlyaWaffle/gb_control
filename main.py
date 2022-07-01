print('Контрольная работа GB: написать программу, которая из имеюшегося массива строк создает'
      '\nновый массив из строк, длина которых больше или равна 3')
input("Нажмите 'Enter' для продолжения")
print("Вводите слова/цифры/числа через пробел ")
list = [ input() for i in range(5)]
print("Текущий массив: ")
print(list)
index = 0
for i in list:
    if len(i) <= 3:
        index += 1

second_array = [0 for i in range(index)]
index = 0
for i in list:
    if len(i) <= 3:
        second_array[index] = i
        index += 1
print(second_array)