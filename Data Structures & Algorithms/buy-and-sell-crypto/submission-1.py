class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>0:
                    profits.append(prices[j]-prices[i])
        if profits==[]:
            return 0
        else:
            return max(profits)
        