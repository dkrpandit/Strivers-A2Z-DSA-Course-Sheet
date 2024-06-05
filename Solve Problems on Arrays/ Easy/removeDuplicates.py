def removeDuplicates(self, nums: List[int]) -> int:
        # dic = {}
        # for i in range(len(nums)):
        #     if nums[i] in dic:
        #         dic[nums[i]]+=1
        #     else:
        #         dic[nums[i]]=1
        # return int(len(dic))
        nums[:] = sorted(set(nums))
        return len(nums)
