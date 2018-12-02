array = [2, 5, 1, 3, -2, 0, 7, 4, 8]
length = len(array)
print(array)
for i in range(0, length):
    thisMin = i
    for j in range(i + 1, length):
        if array[j] < array[thisMin]:
            thisMin = j
    temp = array[i]
    array[i] = array[thisMin]
    array[thisMin] = temp
print(array)
