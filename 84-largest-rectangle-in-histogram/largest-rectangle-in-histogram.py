class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped_value = stack.pop()
                if stack:
                    width = i-stack[-1]-1
                else:
                    width = i
                area = heights[popped_value] * width
                max_area = max(area, max_area)
            stack.append(i)
        return max_area