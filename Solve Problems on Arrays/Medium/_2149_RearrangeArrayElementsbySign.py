def rearrangeArray(self, nums: List[int]) -> List[int]:
        negativeInt = []
        positiveInt = []
        outPut=[]
        n = int(len(nums)/2)
        for i in range(len(nums)):
            if(nums[i]<0):
                negativeInt.append(nums[i])
            else:
                positiveInt.append(nums[i])
        for i in range(n):
            outPut.append(positiveInt[i])
            outPut.append(negativeInt[i])
        return outPut
