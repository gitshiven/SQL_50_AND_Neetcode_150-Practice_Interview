class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]   # start mein empty string
        
        for char in s:
            if char == '(':
                stack.append("")        # naya level shuru
            elif char == ')':
                inner = stack.pop()      # andar wala string nikalo
                stack[-1] += inner[::-1] # reverse karke pichle mein jodo
            else:
                stack[-1] += char        # current level mein add karo
        
        return stack[0]