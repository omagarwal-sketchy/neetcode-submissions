class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        outdict = defaultdict(list)
        for i in strs:
            freqlist=[0]*26
            for j in i:
                freqlist[ord(j)-97]+=1
            outdict[tuple(freqlist)].append(i)
        return list(outdict.values())
        
            

