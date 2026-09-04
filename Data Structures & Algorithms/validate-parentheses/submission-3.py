class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}": "{", ")": "(" , "]": "["}
        st = []



        for char in s:
            if char in mapping:
                if not st or st.pop() != mapping[char]:
                    return False
            else:
                st.append(char)

        return len(st) == 0


                        