class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, number in enumerate(nums):
            match = target - number
            if match in prevMap:
                return [prevMap[match], i]
            prevMap[number] = i
        