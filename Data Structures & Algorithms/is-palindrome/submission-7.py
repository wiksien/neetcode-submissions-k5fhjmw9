import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        if len(s) is 0:
            return True
        L, R = 0, len(s) - 1

        while L < R:
            if (s[L] is s[R]):
                print(s[L], s[R])
                print(L, R)
                L += 1
                R -= 1 
            else:
                return False
        
        return True
        