class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # We initialize with the first element
        current_streak = max_total = nums[0]
        
        for i in range(1, len(nums)):
            # If current_streak is negative, it's better to start fresh 
            # with the current number.
            current_streak = max(nums[i], current_streak + nums[i])
            
            # Keep track of the best streak we've ever seen
            max_total = max(max_total, current_streak)
            
        return max_total