class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def linear_rob(houses):
            prev2, prev1 = 0, 0
            for amount in houses:
                new_rob = max(prev1, amount + prev2)
                prev2 = prev1
                prev1 = new_rob
            return prev1

        return max(linear_rob(nums[:-1]), linear_rob(nums[1:]))