import Project5 as p5


array = p5.irand(100, 200)



def insertionSort(arr): 
    for i in range(1, len(arr)):
        val = arr[i]
        j = i-1
        while( j>= 0) and (arr[j]>val):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = val
    return arr

array = insertionSort(array)