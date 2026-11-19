class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)

        while l != r:
            mid = l + (r - l)//2
            if target in nums[l:mid + 1]:
                r = mid
            elif target in nums[mid + 1:r + 1]:
                l = mid + 1
            else:
                return -1

        return l

        """
        0-5 -> 2 -> 2
        3-5 -> 1 -> 4
        4-6 -> 0 -> 4
        """