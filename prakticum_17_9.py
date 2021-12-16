def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if max(num_sorted) == element:
        return "Введенное число является последним элементом в отсортированном списке." '\n' + "Индекс меньшего элемента:" + str(len(array)-2)
    elif min(num_sorted) == element:
        return "Введенное число является первым элементом в отсортированном списке." '\n' + "Индекс элемента введенного пользователем: " + str(0)
    elif array[middle] == element:
        return "Индекс элемента введенного пользователем:" + str(middle)+'\n' + "Индекс меньшего элемента:" + str(middle-1)
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    elif element > array[middle]:
        return binary_search(array, element, middle + 1, right)

num = list(map(int, input("Введите целые числа через пробел:").split()))
element = int(input("Введите любое целое число : "))
num.append(element)

num_sorted = sorted(num)
print(num_sorted)

element_index = binary_search(num_sorted, element, 0, len(num_sorted)-1)
print(element_index)