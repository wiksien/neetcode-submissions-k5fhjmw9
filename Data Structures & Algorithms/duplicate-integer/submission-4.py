class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for nums_index in range(len(nums)):
            curr_num = nums[nums_index]

            if curr_num in seen:
                return True
            
            seen.add(curr_num)
        
        return False