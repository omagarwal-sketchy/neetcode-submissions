class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r,maxl=0,0,0
        dic=dict()
        while r<len(fruits):
            if len(dic)<=2:
                if fruits[r] in dic:
                    dic[fruits[r]]+=1
                else:
                    dic[fruits[r]]=1  
            while len(dic)>2:
                dic[fruits[l]]-=1
                if dic[fruits[l]]==0:
                    del dic[fruits[l]]
                l+=1
            maxl=max(r-l+1,maxl)
            r+=1
        return maxl

            