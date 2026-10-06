class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        ind=dict()
        for i,n in enumerate(nums1):
            ind[n]=i
        st=[]
        for i in range(len(nums2)):
            while st and nums2[i]>st[-1]:
                val=st.pop()
                res[ind[val]]=nums2[i]
            if nums2[i] in ind:
                st.append(nums2[i])
        return res