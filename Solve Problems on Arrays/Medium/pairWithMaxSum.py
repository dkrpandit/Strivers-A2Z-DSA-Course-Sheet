def pairWithMaxSum(self, arr, N):
        # Your code goes here
        maxSum=-9999999
        for i in range(N-1):
            maxSum=max(maxSum,arr[i]+arr[i+1])
        return maxSum
