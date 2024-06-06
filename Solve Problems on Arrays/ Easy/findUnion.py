def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        dic = {}
        
        for i in range(len(arr1)):
            if arr1[i] in dic:
                dic[arr1[i]]+=1
            else:
                dic[arr1[i]]=1
        for i in range(len(arr2)):
            if arr2[i] in dic:
                dic[arr2[i]]+=1
            else:
                dic[arr2[i]]=1
        list1 = list(dic.keys())
        list1.sort()
        return list1
