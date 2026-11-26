class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0

        # Brute force

        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = min(heights[l], heights[r]) * (r - l)
        #         maxAmount = max(maxAmount, area)

        # return maxAmount

        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxAmount = max(maxAmount, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                    
        return maxAmount



        # l = 0

        # for r in range(len(heights)):
        #     area = min(heights[l], heights[r]) * (r - l)
        #     maxAmount = max(maxAmount, area)

        #     while heights[r] > heights[l]:
        #         l += 1
        
        # return maxAmount