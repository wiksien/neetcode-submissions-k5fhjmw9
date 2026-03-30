class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, number in enumerate(nums):
            diff = target - number
            if diff in hashMap:
                return [hashMap[diff], i]
            else:
                hashMap[number] = i
        