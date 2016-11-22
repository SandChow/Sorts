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
        return array

if __name__=="__main__":
    print insertion_sort(None)

