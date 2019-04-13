import Project5 as p5
import Project6 as p6

array = p5.irand(100, 200)
print ("\nRandom list of 100 numbers from 0 to 200:\n"+str(array)+"\n")

array = p6.insertionSort(array)
print ("Sorted list:\n"+str(array)+"\n")

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

def outputText(item, i):
    if i is not -1:
        print str(item)+" is in position "+ str(i)+ "\n"
    else:
        print str(item) + " is not in the sequence"+"\n"


i1 = int(input("Enter number in list: "))
outputText(i1, binarySearch(array, i1))

i2 = int(input("Enter number not in list: "))
outputText(i2, binarySearch(array, i2))

