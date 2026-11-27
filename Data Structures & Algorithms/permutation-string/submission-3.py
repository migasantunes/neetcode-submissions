class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n)

        s1_map = defaultdict(int)
        for c in s1:
            s1_map[c] += 1

        for r in range(len(s1) - 1, len(s2)):
            l = r - len(s1) + 1

            sub = s2[l:r + 1]

            sub_map = defaultdict(int)
            for c in sub:
                sub_map[c] += 1

            if sub_map == s1_map:
                return True
        
        return False

        # # Sorted
        # s1 = "".join(sorted(s1))
        # for r in range(len(s1) - 1, len(s2)):
        #     l = r - len(s1) + 1

        #     sub = s2[l:r + 1]

        #     if "".join(sorted(sub)) == s1:
        #         return True
        
        # return False