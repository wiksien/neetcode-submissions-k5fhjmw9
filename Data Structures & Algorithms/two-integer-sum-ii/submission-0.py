class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        sum = numbers[L] + numbers[R]

        while sum != target:
            if sum > target:
                R -= 1
            elif sum < target:
                L += 1

            sum = numbers[L] + numbers[R]
        
        return [L + 1, R + 1]

        