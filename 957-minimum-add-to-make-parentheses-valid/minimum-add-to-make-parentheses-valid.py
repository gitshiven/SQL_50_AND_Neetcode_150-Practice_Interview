class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0   # abhi tak unmatched '(' ki ginti
        add = 0           # insert karne padne wale '(' (unmatched ')' ke liye)

        for char in s:
            if char == '(':
                open_needed += 1
            else:  # ')'
                if open_needed > 0:
                    open_needed -= 1   # match ho gaya
                else:
                    add += 1           # is ')' ke liye '(' lagana padega

        return add + open_needed       # bache '(' ke liye ')' lagane padenge