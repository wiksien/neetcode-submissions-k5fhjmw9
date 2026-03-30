class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0

        while index + 1 < len(nums):
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                nums.pop(index)
            else:
                index += 1
        
        return len(nums)
            
        