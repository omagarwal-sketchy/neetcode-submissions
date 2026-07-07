class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        nums+=nums
        res=[]
        for i in range(0,int(len(nums)/2)):
            for j in range(i,i+int(len(nums)/2)-1):
                prod*=nums[j+1]
            res.append(prod)
            prod=1
        return res