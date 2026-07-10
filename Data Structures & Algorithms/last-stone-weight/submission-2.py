class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            max=heapq.heappop(stones)
            secmax=heapq.heappop(stones)
            if secmax>max:
                heapq.heappush(stones,max-secmax)
        stones.append(0)
        return abs(stones[0])