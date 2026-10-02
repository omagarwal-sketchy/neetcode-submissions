class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic={}
        res=set()
        for i,n in enumerate(nums):
            dic[n]=i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if -nums[i]-nums[j] in dic:
                    triplet=tuple(sorted([nums[i],nums[j],-nums[i]-nums[j]]))
                    if dic[-nums[i]-nums[j]]!=i and dic[-nums[i]-nums[j]]!=j:
                        res.add(triplet)
                
        l=[]
        for i in res:
            l.append(i)
        return l