from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.min_cost = float("inf")

        @lru_cache(maxsize=None)
        def takeAPath(index, cur_cost):
            if index >= len(cost):
                print(cur_cost)
                self.min_cost = min(self.min_cost, cur_cost)
                return
            
            if index > -1:
                cur_cost += cost[index]
            
            takeAPath(index + 1, cur_cost)
            takeAPath(index + 2, cur_cost)
        
        takeAPath(-1, 0)

        return self.min_cost
        