class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        seen_indexes = set()

        for _ in range(k):
            cur_max = float("-inf")
            for i, n in enumerate(nums):
                if i not in seen_indexes:
                    if n > cur_max:
                        cur_max = n
                        cur_max_index = i

            seen_indexes.add(cur_max_index)
        
        return cur_max

        