def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        extra = {}
        for i in range(len(nums)): # O(n)
            tmp = target - nums[i] # 0(1)
            if (tmp in extra):
                return [extra[tmp], i]
            extra[nums[i]] = i
            
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if target - nums[i] == nums[j]:
        #             return [i,j]
        # return None
