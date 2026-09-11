class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)  #jab bhi koi position ka element fix karna ho
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_value = stack.pop()
                result[popped_value] = (i - popped_value)
            stack.append(i)
        return result