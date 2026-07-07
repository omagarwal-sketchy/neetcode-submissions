class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=list()
        res=0
        for i in range(0,len(nums)+1):
            l.append(i)
        l=l+nums
        for i in range(len(l)):
            res=res^l[i]
        return res