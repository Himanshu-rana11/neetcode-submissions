class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        st = deque()

        for i in range(n):
            while len(st) > 0 and temperatures[i] > temperatures[st[-1]]:
                prev_index = st.pop()
                result[prev_index] = i - prev_index

            st.append(i)
        return result

