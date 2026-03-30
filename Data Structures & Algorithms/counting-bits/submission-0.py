class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        def countBits(n):
            res = 0
            while n:
                n &= n - 1
                res += 1
            return res
        
        for number in range(n + 1):
            res.append(countBits(number))
        
        return res
        