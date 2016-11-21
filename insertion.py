def insertion_sort(array):
    for i in range(len(array)-1):
        if array[i+1] < array[i]:
            tmp = array[i+1]
            for j in xrange(i+1, 0):
                array[j] = array[j-1]
                print array
            array[0] = tmp
    return array

if __name__=="__main__":
    print insertion_sort([3, 1, 2])

