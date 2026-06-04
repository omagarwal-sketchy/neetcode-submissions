class Solution:
    def isValid(self, s: str) -> bool:
        x=s.replace("{}","").replace("()","").replace("[]","")
        if x == "()" or x == "[]" or x == "{}" or x == "":
            return True
        else:
            return False
        