def leaders(self, A, N):
        #Code here
        arr=[]
        arr.append(A[N-1])
        maxi = A[N-1]
        for i in range(N-2,-1,-1): # (start,end,gap)
            if(maxi<=A[i]):
                maxi=A[i]
                arr.append(maxi)
        arr.reverse()
        return arr
