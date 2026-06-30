class Solution:
    def climbStairs(self, n: int) -> int:
        count=1
        x=n
        count1=n
        count2=0
        while count1>=2:
            x-=1
            count1-=2
            count2+=1
            count+=math.factorial(x)/(math.factorial(count1)*math.factorial(count2))
        return int(count)