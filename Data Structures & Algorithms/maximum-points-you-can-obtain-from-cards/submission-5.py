class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=0
        for i in range(0,k):
            lsum+=cardPoints[i]
        rsum=0
        res=rsum+lsum
        for i in range(0,k+1):
            sumi=lsum+rsum
            lsum-=cardPoints[k-i-1]
            rsum+=cardPoints[len(cardPoints)-i-1]
            res=max(res,sumi)
        return res