class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for _ in range(k):
            cur_max = nums.pop(nums.index(max(nums)))
        
        return cur_max

        