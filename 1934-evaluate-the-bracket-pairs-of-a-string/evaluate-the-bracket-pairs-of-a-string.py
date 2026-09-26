class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_map = {}
        for key, value in knowledge:
            knowledge_map[key] = value
        
        #dictionary banayi taki lookup O(1) hojaye, list mai O(n) hoti
        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                key = ""
                i += 1                      # '(' ke baad se shuru karo
                while s[i] != ')':
                    key += s[i]              # character collect karo
                    i += 1
        # ab key complete hai, ')' pe hain
        
                if key in knowledge_map:
                    result.append(knowledge_map[key])
                else:
                    result.append('?')
        
                i += 1                       # ')' cross karo
            else:
                result.append(s[i])          # normal character
                i += 1

        return ''.join(result)
