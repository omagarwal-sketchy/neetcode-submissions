class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        res,length=0,0
        for i in nums:
            if i-1 not in nums:
                length=0
                while (i+length) in nums:
                    length+=1    
            if length>res:
                res=length
        return res