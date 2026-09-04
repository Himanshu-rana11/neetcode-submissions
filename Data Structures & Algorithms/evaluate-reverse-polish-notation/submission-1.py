class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        if not tokens:
            return 0
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                st.append(int(token))
            else:
                b = st.pop()
                a = st.pop()
                
                if token == "+":
                    st.append(a + b)
                elif token == "-":
                    st.append(a - b)
                elif token == "*":
                    st.append(a * b)
                elif token == "/":
                    # int(a / b) truncates toward zero as required
                    st.append(int(a / b))
            
        return st.pop()
            