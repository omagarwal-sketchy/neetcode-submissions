class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def subarr(nums,goal):
            if goal<0:
                return 0
            l,r,count,add=0,0,0,0
            while r<len(nums):
                add+=nums[r]
                while add>goal:
                    add-=nums[l]
                    l+=1
                count=count+(r-l+1)
                r+=1
            return count
        return subarr(nums,goal)-subarr(nums,goal-1)