class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for step in range(len(cost)-3,-1,-1):
            cost[step]+=min(cost[step+1],cost[step+2])
        return min(cost[0],cost[1])