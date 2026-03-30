import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_characters = string.ascii_lowercase + '0123456789'

        L = 0
        R = len(s) - 1

        while L < R:
            while s[L].lower() not in valid_characters and L < R:
                L += 1
            while s[R].lower() not in valid_characters and L < R:
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        
        return True
            
        