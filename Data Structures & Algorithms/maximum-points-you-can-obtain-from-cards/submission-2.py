class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=len(cardPoints)-k
        r=len(cardPoints)-1
        res=sum(cardPoints[0:k])
        temp=sum(cardPoints[len(cardPoints)-k:len(cardPoints)])
        res=max(res,temp)
        cardPoints+=cardPoints
        for r in range(len(cardPoints)//2-1,len(cardPoints)//2+k-1):
            temp=temp-cardPoints[l]+cardPoints[r+1]
            res=max(res,temp)
            l+=1
        return res
        