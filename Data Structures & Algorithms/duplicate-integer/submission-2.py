class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        disset=set(nums)
        if len(disset)==len(nums) :
            return False
        else:
            return True

        