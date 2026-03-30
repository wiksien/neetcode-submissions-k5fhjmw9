class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def traverseDecisionTree(current_decision_pointer: int, result: List, temp_comb: List[int]):
            if current_decision_pointer > len(nums) - 1:
                return

            comb_sum = sum(temp_comb)

            if comb_sum > target:
                temp_comb.pop()
                return
            
            if comb_sum == target:
                result.append(temp_comb.copy())
                temp_comb.pop()
                return
            
            traverseDecisionTree(current_decision_pointer, result, temp_comb + [nums[current_decision_pointer]])
            traverseDecisionTree(current_decision_pointer + 1, result, temp_comb)

            return result
        
        return traverseDecisionTree(0, [], [])