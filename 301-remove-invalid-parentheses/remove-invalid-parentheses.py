class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Step 1: kitne '(' aur ')' remove karne hain
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        result = set()

        def dfs(i, left_count, right_count, left_rem, right_rem, path):
            if i == len(s):
                if left_rem == 0 and right_rem == 0:
                    result.add(''.join(path))
                return

            ch = s[i]

            # Choice 1: is bracket ko HATAO
            if ch == '(' and left_rem > 0:
                dfs(i + 1, left_count, right_count, left_rem - 1, right_rem, path)
            elif ch == ')' and right_rem > 0:
                dfs(i + 1, left_count, right_count, left_rem, right_rem - 1, path)

            # Choice 2: is char ko RAKHO
            path.append(ch)
            if ch != '(' and ch != ')':
                dfs(i + 1, left_count, right_count, left_rem, right_rem, path)
            elif ch == '(':
                dfs(i + 1, left_count + 1, right_count, left_rem, right_rem, path)
            elif right_count < left_count:      # ')' tabhi rakho jab pending '(' ho
                dfs(i + 1, left_count, right_count + 1, left_rem, right_rem, path)
            path.pop()

        dfs(0, 0, 0, left_rem, right_rem, [])
        return list(result)