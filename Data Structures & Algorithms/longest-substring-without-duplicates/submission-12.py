class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap=[0]*128
        l,r=0,0
        res=0
        while r<len(s):
            if hashmap[ord(s[r])]<1:
                hashmap[ord(s[r])]+=1
                res=max(res,r-l+1)
                r+=1
            else:
                hashmap[ord(s[l])]-=1
                l+=1
        return res