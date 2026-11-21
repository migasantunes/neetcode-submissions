class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window -> open until an error -> close until error is corrected
        
        seen = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in seen: # Corrected the window
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest