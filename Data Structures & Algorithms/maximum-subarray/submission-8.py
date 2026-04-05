class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_streak = max_total = nums[0]
        
        for i in range(1, len(nums)):
            current_streak = max(nums[i], current_streak + nums[i])
            
            max_total = max(max_total, current_streak)
            
        return max_total