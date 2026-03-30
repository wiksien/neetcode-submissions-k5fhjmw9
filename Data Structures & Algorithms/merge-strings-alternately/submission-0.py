class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        W1, W2 = 0, 0

        output = ""

        while W1 < len(word1) or W2 < len(word2):
            if W1 < len(word1):
                output += word1[W1]
            
            if W2 < len(word2):
                output += word2[W2]

            W1 += 1
            W2 += 1
        
        return output
        