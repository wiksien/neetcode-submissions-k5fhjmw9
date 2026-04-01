class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)

        for index in range(n - 2, -1, -1):
            cost[index] += min(cost[index + 1], cost[index + 2])
        
        return min(cost[0], cost[1])