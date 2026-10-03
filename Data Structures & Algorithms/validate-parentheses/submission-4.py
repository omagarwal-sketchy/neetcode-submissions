class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else: 
                if not stack:
                    return False           
                if stack[-1]=="(" and s[i]==")" or stack[-1]=="[" and s[i]=="]" or stack[-1]=="{" and s[i]=="}":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
