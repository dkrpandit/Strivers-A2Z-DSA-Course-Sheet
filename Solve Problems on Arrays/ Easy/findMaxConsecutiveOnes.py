def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        first = 0
        second = 0

        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                first+=1
            else:
                second = max(first,second)
                first=0
        first = max(first,second)
        return first
