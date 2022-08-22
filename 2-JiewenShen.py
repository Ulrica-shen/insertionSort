def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)  #math.floor，Take down the whole，So 2.3 is equal to 2，Math.ceil()Round up, math.round ()
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right)) 	#Recursive decomposition
#Compare the left and right arrays (already sorted) pairwise, and add the smallest one to the new result array
def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0));
    return result

#perform
print(mergeSort(list))
