def insertion_sort(array):
    if array:
        for i in xrange(1, len(array)):
            if array[i] < array[i-1]:
                tmp = array[i]
                j = i
                while tmp < array[j-1] and j > 0:
                    array[j] = array[j-1]
                    j -= 1
                array[j] = tmp

if __name__=="__main__":
    unsorted = None
    insertion_sort(unsorted)
    assert(unsorted == None), "Still not sorted"

    unsorted = [1]
    insertion_sort(unsorted)
    assert(unsorted == [1]), "Still not sorted"

    unsorted = [1, 1]
    insertion_sort(unsorted)
    assert(unsorted == [1, 1]), "Still not sorted"

    unsorted = [-1, -2, -3, -4, -5]
    insertion_sort(unsorted)
    assert(unsorted == [-5, -4, -3, -2, -1]), "Still not sorted"
