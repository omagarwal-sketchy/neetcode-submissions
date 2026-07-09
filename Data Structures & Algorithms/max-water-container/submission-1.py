class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res,temp=0,0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                temp=min(heights[i],heights[j])*(j-i)
                res=max(res,temp)
        return res
            