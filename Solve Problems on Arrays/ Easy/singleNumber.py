def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        if(len(nums)==1 or len(nums)==2):
            return nums[0]
        else:
            for key in dic.keys():
                if dic[key] == 1:
                    return key
