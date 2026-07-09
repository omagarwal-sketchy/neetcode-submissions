class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max=float('-inf')
        secmax=float('-inf')
        for i in stones:
            if i>=max:
                secmax=max
                max=i
            elif i>secmax:
                secmax=i
        if len(stones)==0:
            return 0
        elif len(stones)==1:
            return stones[0]
        if max!=secmax:
            stones.append(max-secmax)
        stones.remove(max)
        stones.remove(secmax)
        return self.lastStoneWeight(stones)