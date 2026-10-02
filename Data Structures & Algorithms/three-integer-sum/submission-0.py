class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic={}
        l=[]
        for i,n in enumerate(nums):
            dic[n]=i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if -nums[i]-nums[j] in dic and sorted([nums[i],nums[j],-nums[i]-nums[j]]) not in l and dic[-nums[i]-nums[j]]!=i and dic[-nums[i]-nums[j]]!=j :
                    l.append(sorted([nums[i],nums[j],-nums[i]-nums[j]]))
        return l