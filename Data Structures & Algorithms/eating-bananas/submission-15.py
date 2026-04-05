class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1 
        R = max(piles)

        while L < R:
            curr_rate = (L + R) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += (pile + curr_rate - 1) // curr_rate
            
            if total_hours > h:
                L = curr_rate + 1
            else:
                R = curr_rate
        
        return L


