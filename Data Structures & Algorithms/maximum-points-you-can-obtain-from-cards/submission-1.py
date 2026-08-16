class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=len(cardPoints)-k
        r=len(cardPoints)-1
        res=sum(cardPoints[0:k])
        cardPoints+=cardPoints
        for r in range(len(cardPoints)//2-1,len(cardPoints)//2+k-1):
            res=max(res,sum(cardPoints[l:r+1]))
            l+=1
        return res