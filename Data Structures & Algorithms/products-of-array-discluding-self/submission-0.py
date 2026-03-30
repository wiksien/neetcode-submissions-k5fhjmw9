from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for number in nums:
            temp_array_without_target = nums.copy()
            temp_array_without_target.remove(number)
            result.append(reduce(lambda x, y: x * y, temp_array_without_target))
        return result
        