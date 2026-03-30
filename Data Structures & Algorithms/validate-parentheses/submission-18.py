class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        stack.append(s[0])

        opposite = ""
        
        for symbol in s[1:]:
            match symbol:
                case "(":
                    opposite = ")"
                case ")":
                    opposite = "("
                case "[":
                    opposite = "]"
                case "]":
                    opposite = "["
                case "{":
                    opposite = "}"
                case "}":
                    opposite = "{"
                case _:
                    opposite = None
            
            if stack != [] and opposite == stack[-1]:
                stack.pop()
            elif symbol in ["(","{","["]:
                stack.append(symbol)
            else:
                return False

        return stack == []
            
            
        