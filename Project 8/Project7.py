import Project5 as p5
import Project6 as p6

# Binary Search
# Returns index of item if found in location otherwise returns -1
def binarySearch(arr, item):
    first = 0
    last = len(arr)-1

    while first<=last:
        mid = (first + last)//2
        if arr[mid] == item:
            return mid
        else:
            if arr[mid] > item:
                last = mid-1
            else:
                first = mid+1

    return -1
