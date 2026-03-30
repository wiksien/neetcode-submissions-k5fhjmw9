from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def xor(a, b):
            return a ^ b
        
        return reduce(xor, nums)

        