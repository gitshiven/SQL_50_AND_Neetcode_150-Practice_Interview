class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow_2 = 0
        while slow != slow_2:
            slow = nums[slow]
            slow_2 = nums[slow_2]
        return slow