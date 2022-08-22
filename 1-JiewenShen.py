def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
	
        key = arr[i]   #Number to be inserted
  
        j = i-1	#The previous number to be inserted
	#Compare all the way forward, if the subscript does not overflow and a number larger than the number to be inserted is found
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j]  #Larger numbers move back
                j -= 1		#Go ahead and compare
        arr[j+1] = key 		#Place the number to be inserted
  
  
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("排序后的数组:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])
