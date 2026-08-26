class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for x in s :
            if x in "([{":
               stack.append(x)
            elif not stack:
                return False
            elif pairs [stack[-1]] != x:
                return False 

            else:
                stack.pop() 
        return not stack 
