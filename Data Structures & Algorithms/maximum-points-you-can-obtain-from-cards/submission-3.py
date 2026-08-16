class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res=sum(cardPoints[0:k])
        for i in range(0,k+1):
            lsum=sum(cardPoints[0:k-i])
            rsum=sum(cardPoints[len(cardPoints):len(cardPoints)-i-1:-1])
            sumi=lsum+rsum
            res=max(res,sumi)
        return res