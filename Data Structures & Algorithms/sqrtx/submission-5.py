class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        res = 0

        while L <= R:
            mid = (L + R) // 2
            potential_result = mid * mid

            if potential_result > x:
                R = mid - 1
            elif potential_result < x:
                res = mid
                L = mid + 1
            else:
                return mid
        
        return res