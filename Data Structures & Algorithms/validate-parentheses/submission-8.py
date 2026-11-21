class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        par = {")": "(",
               "]": "[",
               "}": "{"}

        for p in s:
            if p in par.values():
                stack.append(p)

            elif p in par.keys():
                if not stack: return False

                out = stack.pop()
                if out != par[p]:
                    return False
        
        return True if not stack else False