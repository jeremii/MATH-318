import Project5 as p5


array = p5.irand(100, 200)

def insertionSort(arr): 
  
    # For every element in the array, do this:
    for i in range(1, len(arr)): 
        # assign key as the array item in this current iteration
        key = arr[i] 
  
        # j will be one iteration back
        j = i-1
        # while j is >= 0 and the arr[i] is less than arr[j]
        while j >=0 and key < arr[j] : 
            #insertion sort
            arr[j+1] = arr[j] 
            # j decrements by 1
            j -= 1
        arr[j+1] = key 
    return arr

array = insertionSort(array)

for i in range(len(array)):
    print array[i]