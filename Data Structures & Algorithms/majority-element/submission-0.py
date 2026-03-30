from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = Counter(nums)

        return max(hash_map, key=hash_map.get)
        