class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=list()
        digstr=""
        for i in digits:
            digstr+=str(i)
        summed=int(digstr)+1
        for j in str(summed):
            l.append(j) 
        return l
