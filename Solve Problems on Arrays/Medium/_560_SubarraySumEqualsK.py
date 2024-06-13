def subarraySum(self, nums: List[int], k: int) -> int:
        # Time Limit Exceeded -> 83 / 93 testcases passed
        nOfSum=0
        for i in range(len(nums)):
            aSum=0
            for j in range(i,len(nums)):
                aSum+=nums[j]
                if(aSum==k):
                    nOfSum+=1
        return nOfSum
