class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = deque()
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        counter = 1
        for p,s in pair:
            t = (target-p)/s
            if st:
                if st[-1] < t:
                    st.pop()
                    st.append(t)
                    counter +=1
            else:
                st.append(t)
        return counter
        