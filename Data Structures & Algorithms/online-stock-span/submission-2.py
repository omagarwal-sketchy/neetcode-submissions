class StockSpanner:

    def __init__(self):
        self.st=[]

    def next(self, price: int) -> int:
        self.st.append(price)
        def pge(arr):
            st=[]
            res=[-1]*len(arr)
            for i in range(len(arr)):
                while st and arr[st[-1]]<=arr[i]:
                    st.pop()
                if st:
                    res[i]=st[-1]
                st.append(i)
            return res
        res=pge(self.st)
        i=len(res)-1
        return i-res[i]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)