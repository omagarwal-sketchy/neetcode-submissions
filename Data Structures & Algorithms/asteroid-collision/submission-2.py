class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in range(len(asteroids)):
            while st and asteroids[i]<0 and st[-1]>0 and -asteroids[i]>abs(st[-1]):
                st.pop()
            if st and asteroids[i]<0 and st[-1]>0 and asteroids[i]+st[-1]==0:
                st.pop()
                continue
            if st and asteroids[i]<0 and st[-1]>0 and -asteroids[i]<abs(st[-1]):
                continue
            st.append(asteroids[i])

        return st