class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                L = mid + 1

            if target < nums[mid]:
                R = mid - 1

        return -1
        