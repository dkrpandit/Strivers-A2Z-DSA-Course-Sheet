def print2largest(self,arr, n):
		max = arr[0]
		min = -1
		for i in range(1,n):
		    if(arr[i]>max):
		        max = arr[i]
	  for i in range(n):
      if(arr[i]>min and max!=arr[i]):
        min = arr[i]
    
	  return min
