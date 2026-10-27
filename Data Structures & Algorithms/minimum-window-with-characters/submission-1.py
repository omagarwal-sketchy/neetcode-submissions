class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        thash={}
        r,l=0,0
        res=0
        resr,resl=0,0
        for i in t:
            thash[i]=1+thash.get(i,0)
        shash={}
        have,need=0,len(t)
        l=0
        reslen=float('inf')
        res=[0,0]
        for r in range(len(s)):
            shash[s[r]]=1+shash.get(s[r],0)
            if s[r] in thash and shash[s[r]]<=thash[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                shash[s[l]]-=1
                if s[l] in thash and shash[s[l]]<thash[s[l]]:
                    have-=1
                l+=1
        l,r=res
        if reslen==float('inf'):
            return ""
        else:
            return s[l:r+1]
    

