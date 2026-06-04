class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        for i in range(len(prices)-1):
            maxprof=max(maxprof,max(prices[i+1:len(prices)])-prices[i])
        return maxprof