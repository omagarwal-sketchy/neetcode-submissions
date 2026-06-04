class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[]
        try:
            for i in range(len(prices)):
                for j in range(i+1,len(prices)):
                    if prices[j]-prices[i]>0:
                        profits.append(prices[j]-prices[i])
            return max(profits)
        except:
            return 0