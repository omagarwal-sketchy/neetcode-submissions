class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=dict()
        for i in nums:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic.update({i:1})
        l=list()    
        for num,frequency in dic.items():
            l.append([num,frequency])
        l.sort(key=lambda x: x[1],reverse=True)
        ret=[]
        for j in range(0,k):
            ret.append(l[j][0])
        return ret
        