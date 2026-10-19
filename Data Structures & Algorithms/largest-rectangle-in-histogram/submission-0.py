class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def pse(heights):
            st=[]
            res=[-1]*len(heights)
            for i in range(len(heights)):
                while st and heights[st[-1]]>=heights[i]:
                    st.pop()
                if st:
                    res[i]=st[-1]
                st.append(i)
            return res
        def nse(heights):
            st=[]
            res=[len(heights)]*len(heights)
            for i in range(len(heights)-1,-1,-1):
                while st and heights[st[-1]]>=heights[i]:
                    st.pop()
                if st:
                    res[i]=st[-1]
                st.append(i)
            return res
        p=pse(heights)
        n=nse(heights)
        area=heights[0]
        for i in range(len(heights)):
            area=max(area,heights[i]*(n[i]-p[i]-1))
        return area




