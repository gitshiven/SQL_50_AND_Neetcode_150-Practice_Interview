class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []   # '(' ke indices
        star_stack = []   # '*' ke indices

        # Phase 1: poori string traverse karo
        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:  # ')'
                if open_stack:
                    open_stack.pop()      # pehle asli '('
                elif star_stack:
                    star_stack.pop()      # nahi toh '*' ko '(' maano
                else:
                    return False          # koi match nahi

        # Phase 2: bache hue '(' ko '*' (as ')') se close karo
        while open_stack and star_stack:
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False              # '*' '(' se pehle hai

        return not open_stack             # '(' bacha toh False