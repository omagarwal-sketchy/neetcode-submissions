class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            dic={}
            l,r=0,0
            res=0
            while r<len(nums):
                if nums[r] in dic:
                    dic[nums[r]]+=1
                else:
                    dic[nums[r]]=1
                while len(dic)>k:
                    dic[nums[l]]-=1
                    if dic[nums[l]]==0:
                        del dic[nums[l]]
                    l+=1
                res+=r-l+1
                r+=1
            return res
        return atMost(k)-atMost(k-1)
                
                