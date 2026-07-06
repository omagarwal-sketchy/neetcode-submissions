class Solution:
    def countBits(self, n: int) -> List[int]:
        def count1(x):
            c=0
            while x>=1:
                if x%2==1:
                    c+=1
                x//=2
            return c
        output=list()
        for i in range(0,n+1):
            output.append(count1(i))
        return output
        