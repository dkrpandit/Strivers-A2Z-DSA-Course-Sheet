def maxSubArray(self, nums: List[int]) -> int:
        """
        maxi = -999999
        for i in range(len(nums)):
            sum1=0
            for j in range(i,len(nums)):
                sum1+=nums[j]
                maxi = max(maxi,sum1)
        return maxi
        # Time Limit Exceeded
        """
        """
        # Kadane's Algorithm
        # not working for -ve elements
        maxSum=0
        curSum=0
        for i in range(len(nums)):
            curSum+=nums[i]
            if(curSum>maxSum):
                maxSum=curSum
            if(curSum<0):
                curSum=0
        return maxSum
        """
        if not nums:
            return 0
        maxSum=nums[0]
        curSum=nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i],curSum+nums[i])
            maxSum = max(curSum,maxSum)
        return maxSum
