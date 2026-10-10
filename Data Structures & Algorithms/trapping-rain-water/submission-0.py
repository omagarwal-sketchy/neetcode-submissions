class Solution:
    def trap(self, height: List[int]) -> int:
        total,temp=0,0
        maxl=[height[0]]*len(height)
        maxr=[height[-1]]*len(height)
        for i in range(1,len(height)):
            maxl[i]=max(maxl[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            maxr[i]=max(maxr[i+1],height[i])
        for i in range(0,len(height)):
            temp=min(maxl[i],maxr[i])-height[i]
            if temp>0:
                total+=temp
        return total
