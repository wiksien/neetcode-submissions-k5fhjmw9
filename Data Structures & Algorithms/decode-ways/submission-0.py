class Solution:
    def numDecodings(self, s: str) -> int:
        string_bound = len(s)

        def decisionDecode(string_index, result):
            if string_index == string_bound:
                return result + 1
            
            if s[string_index] == "0":
                return result
            
            ways = decisionDecode(string_index + 1, result)
            
            if string_index + 1 < string_bound:
                two_digit = int(s[string_index : string_index + 2])
                if 10 <= two_digit <= 26:
                    ways += decisionDecode(string_index + 2, result)
            
            return ways
        
        return decisionDecode(0, 0)
        