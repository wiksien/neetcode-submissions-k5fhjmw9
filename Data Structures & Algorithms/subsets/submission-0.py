class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      curr_subset = []
      total_subsets = []

      def add_or_not(curr_subset: List[int], number_idx: int):
        if number_idx == len(nums):
          total_subsets.append(curr_subset.copy())
          return curr_subset
        
        add_or_not(curr_subset, number_idx + 1)

        curr_subset.append(nums[number_idx])
        add_or_not(curr_subset, number_idx + 1)
        curr_subset.pop()

      add_or_not(curr_subset, 0)

      return total_subsets
        