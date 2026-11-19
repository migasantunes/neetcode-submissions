class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)

        res = 1
        l, r = 0, 0

        s = list(s)
        if len(s) == 0: return 0

        leng = 1
        count[s[l]] += 1
        while r != len(s)-1:
            r += 1
            count[s[r]] += 1
            leng += 1

            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
                leng -= 1
        
            res = max(res, leng)

        return res