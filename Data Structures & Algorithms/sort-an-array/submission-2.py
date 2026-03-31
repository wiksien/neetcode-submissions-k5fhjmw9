import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(L, R):
            if L >= R:
                return

            pivot_idx = random.randint(L, R)
            nums[pivot_idx], nums[R] = nums[R], nums[pivot_idx]

            pivot_value = nums[R]
            slow_pointer = L

            for jump_index in range(L, R):
                if nums[jump_index] <= pivot_value:
                    nums[slow_pointer], nums[jump_index] = nums[jump_index], nums[slow_pointer]
                    slow_pointer += 1
            
            nums[slow_pointer], nums[R] = nums[R], nums[slow_pointer]
            
            quickSort(L, slow_pointer - 1)
            quickSort(slow_pointer + 1, R)
        
        quickSort(0, len(nums) - 1)

        return nums