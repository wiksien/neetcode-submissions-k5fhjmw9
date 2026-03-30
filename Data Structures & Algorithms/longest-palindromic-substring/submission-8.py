class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        result = ""

        def expand(l, r):
            # Expand as long as pointers are in bounds and chars match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # Return the valid palindrome found (slices back to valid range)
            return s[l + 1:r]

        for i in range(len(s)):
            # Case 1: Odd length (center is one char, e.g., 'a')
            p1 = expand(i, i)
            # Case 2: Even length (center is between two chars, e.g., 'aa')
            p2 = expand(i, i + 1)
            
            # Update result if a longer palindrome is found
            result = max(result, p1, p2, key=len)

        return result
        