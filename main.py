list = [ input() for i in range(5)]
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