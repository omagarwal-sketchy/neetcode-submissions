class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]
        post=1
        for j in range(len(nums)-2,-1,-1):
            res[j]*=post*nums[j+1]
            post*=nums[j+1]
        return res