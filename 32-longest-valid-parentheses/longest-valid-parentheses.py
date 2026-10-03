class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        stack = [-1]
        for char in range(len(s)):
            length = 0
            if s[char] == '(':
                stack.append(char)
            elif s[char] == ')':
                stack.pop()
                if stack:
                    length = char - stack[-1]
                    max_len = max(max_len, length)
                else :
                    stack.append(char)
        return max_len

