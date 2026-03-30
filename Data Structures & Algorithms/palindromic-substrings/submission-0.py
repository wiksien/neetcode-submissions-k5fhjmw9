class Solution:
    def countSubstrings(self, s: str) -> str:
        if not s:
            return 0
        
        result = []

        def expand(l, r, result):
            # Expand as long as pointers are in bounds and chars match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                result.append(s[l + 1:r])
            # Return the valid palindrome found (slices back to valid range)

        for i in range(len(s)):
            # Case 1: Odd length (center is one char, e.g., 'a')
            expand(i, i, result)
            # Case 2: Even length (center is between two chars, e.g., 'aa')
            expand(i, i + 1, result)

            print(result)
            
            # Update result if a longer palindrome is found

        return len(result)
        
        