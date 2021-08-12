
def sort(array):
    if not array or len(array) <= 1:
        return array # nothing to sort

    index = 0
    swapped = True
    while index < len(array) and swapped:
        swapped = False
        other_index = index + 1
        while other_index < len(array):
            if array[index] > array[other_index]:
                temp = array[index]
                array[index] = array[other_index]
                array[other_index] = temp
                swapped = True

            other_index += 1
        index += 1


    return array
