class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, skip = 0, 0

        for house in nums:
            cur_rob = house + skip

            cur_skip = max(skip, rob)

            rob = cur_rob
            skip = cur_skip
        
        return max(rob, skip)
        