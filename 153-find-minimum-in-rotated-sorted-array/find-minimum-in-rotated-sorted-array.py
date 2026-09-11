class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(1) Initialization - Best Practice
        res = float('inf') 
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            k = nums[mid]
            res = min(k, res)

            if k > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return res
