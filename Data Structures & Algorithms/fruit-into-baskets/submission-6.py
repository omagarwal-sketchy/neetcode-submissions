class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r=0,0
        res=0
        while r<len(fruits):
            if len(set(fruits[l:r+1]))<=2:
                res=max(res,r-l+1)
                r+=1
                continue
            else:
                l+=1
        return res
                