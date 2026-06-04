class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped=[]
        for j in s:
            if j.isalnum():
                stripped.append(j.lower())
        sum=0
        for i in range(len(stripped)):
            if stripped[i]==stripped[len(stripped)-1-i]:
                sum=sum+1
        if sum==len(stripped):
            return True
        else:
            return False
                    