class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        res=0
        countarr=[0]*26
        for r in range(len(s)):
            countarr[ord(s[r])-65]+=1
            if r-l+1-max(countarr)<=k:
                res=max(res,r-l+1)
            else:
                countarr[ord(s[l])-65]-=1
                l+=1
        return res
