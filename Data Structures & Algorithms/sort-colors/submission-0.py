from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_count = Counter(nums)
        print(nums_count)

        for index in range(len(nums)):
            if nums_count[0] > 0:
                nums[index] = 0
                nums_count[0] -= 1
            elif nums_count[1] > 0:
                nums[index] = 1
                nums_count[1] -= 1
            else:
                nums[index] = 2
        
        