def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) #if k is greater than length of nums
        newList = []
        for i in range(len(nums)-k,len(nums)):
            newList.append(nums[i])
        for i in range(len(nums)-k):
            newList.append(nums[i])
        for i in range(len(nums)):
            nums[i]=newList[i]
