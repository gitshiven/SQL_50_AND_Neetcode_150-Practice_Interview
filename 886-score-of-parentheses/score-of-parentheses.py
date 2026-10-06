class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(score)    # bahar ka score save karo
                score = 0              # naya level, 0 se shuru
            else:  # ')'
                if s[i-1] == '(':      # "()" case
                    score = stack.pop() + 1
                else:                  # nested "(A)" case
                    score = stack.pop() + 2 * score

        return score