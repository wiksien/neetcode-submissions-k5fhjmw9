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
            
            if stack != [] and opposite == stack[0]:
                stack.pop(0)
            elif symbol in ["(","{","["]:
                stack.insert(0, symbol)
            else:
                return False

        return stack == []
            
            
        