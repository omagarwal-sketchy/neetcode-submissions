class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssorted=list(s)
        ssorted.sort()
        tsorted=list(t)
        tsorted.sort()
        if ssorted==tsorted:
            return True
        else:
            return False
        