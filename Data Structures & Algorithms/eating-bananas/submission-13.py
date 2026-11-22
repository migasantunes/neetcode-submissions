class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max k would be max(piles) -> eat in len(piles) hours

        def canEat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        l, r = 1, max(piles)
        minK = max(piles)

        # 1, 2, 3, 4
        while l <= r:
            k = l + ((r - l) // 2) 
            if canEat(k):
                r = k - 1
                minK = k
            else:
                l = k + 1
        
        return minK