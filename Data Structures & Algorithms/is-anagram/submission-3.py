class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cars = defaultdict(int)

        for c in s:
            cars[c] += 1
        
        for c in t:
            cars[c] -= 1

        for val in cars.values():
            if val != 0:
                return False
        
        return True