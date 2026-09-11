class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        final_speed = float('inf')
        while l<=r:
            mid = l + ((r-l)//2)
            sum_of_hours = 0
            for i in piles:
                sum_of_hours += math.ceil(i/mid)
            if sum_of_hours <= h:
                final_speed = min(mid, final_speed)
                r = mid - 1
            else:
                l = mid + 1
        return final_speed
