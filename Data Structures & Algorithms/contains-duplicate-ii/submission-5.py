class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums) and k != 1:
            return True

        l, r = 0, k

        while r < len(nums):
            for r_temp in range(l + 1, r + 1):
                if nums[l] == nums[r_temp]:
                    return True
            l += 1
            r += 1
        
        return False
        
        