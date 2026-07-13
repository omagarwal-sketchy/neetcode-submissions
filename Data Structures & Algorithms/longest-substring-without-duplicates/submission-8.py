class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        templ=[]
        res=0
        for i in range(0,len(s)):
            templ=[]
            for j in range(i,len(s)):
                if s[j] in templ:
                    break
                templ.append(s[j])
            res=max(len(templ),res)
        return res