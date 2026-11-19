class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {")": "(",
                "]": "[",
                "}": "{"}

        for c in s:
            if c in pair.values():
                stack.append(c)
            elif c in pair.keys() and stack:
                if stack.pop() != pair[c]:
                    return False
            else:
                return False
        
        if len(stack) != 0: return False

        return True