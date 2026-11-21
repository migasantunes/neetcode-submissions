class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cars = defaultdict(int)

        if len(s) != len(t):
            return False

        for c in s:
            cars[c] += 1
        
        for c in t:
            if cars[c] == 0:
                return False
            cars[c] -= 1
        
        return True