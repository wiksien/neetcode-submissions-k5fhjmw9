# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n

        mid = (L + R) // 2
        guessed_num = guess(mid)

        while guessed_num != 0:
            if guessed_num == -1:
                R = mid - 1
            else:
                L = mid + 1
            
            mid = (L + R) // 2
            guessed_num = guess(mid)
        
        return mid
        