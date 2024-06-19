def isAnagram(self, s: str, t: str) -> bool:
        # for s
        hmapS = {}
        for i in s:
            if i in hmapS:
                hmapS[i]+=1
            else:
                hmapS[i]=1
        # for t
        hmapT={}
        for i in t:
            if i in hmapT:
                hmapT[i]+=1
            else:
                hmapT[i]=1
        if(len(s)!=len(t)):
            return False
        elif(hmapT==hmapS):
            return True
