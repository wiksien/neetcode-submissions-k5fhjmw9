# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n

        M = (R + L) // 2

        num = guess(M)

        while num != 0:
            if num == 1:
                L = M + 1
            elif num == -1:
                R = M - 1
            
            M = (R + L) // 2
            num = guess(M)
        
        return M