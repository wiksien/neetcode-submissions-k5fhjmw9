from functools import reduce

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.result = 0

        def xor(a, b):
            return a ^ b

        def backtrack(temp_nums, index):
            if index > len(nums) - 1:
                if len(temp_nums) != 0:
                    self.result += reduce(xor, temp_nums)
                return
            
            backtrack(temp_nums, index + 1)

            temp_nums.append(nums[index])
            backtrack(temp_nums, index + 1)
            temp_nums.pop()
        
        backtrack([], 0)

        return self.result
            