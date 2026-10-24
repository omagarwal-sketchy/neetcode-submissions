class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while k and st and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        if k:
            del st[-k:]
        return "".join(st).lstrip("0") or "0"

