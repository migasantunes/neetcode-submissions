class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sorted

        s1 = "".join(sorted(s1))
        for r in range(len(s1) - 1, len(s2)):
            l = r - len(s1) + 1

            sub = s2[l:r + 1]

            if "".join(sorted(sub)) == s1:
                return True
        
        return False