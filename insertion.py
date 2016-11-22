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
    unsorted = [3, 1, 5]
    insertion_sort(unsorted)
    assert(unsorted == [1, 3, 5]), "Still not sorted!"
