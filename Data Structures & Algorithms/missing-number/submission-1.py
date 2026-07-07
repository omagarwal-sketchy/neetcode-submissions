class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=list()
        for i in range(0,len(nums)+1):
            l.append(i)
        for i in nums:
            l.remove(i)
        return l[0]