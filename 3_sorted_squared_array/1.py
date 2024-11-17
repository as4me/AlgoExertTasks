def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i] = array[i] * array[i]
    return sorted(array)

array = [1, 2, 3, 5, 6, 8, 9]
print(sortedSquaredArray(array))
