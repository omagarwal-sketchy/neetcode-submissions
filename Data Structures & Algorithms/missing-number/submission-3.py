class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=list()
        for i in range(len(nums)+1):
            l.append(i)
        return sum(l)-sum(nums)