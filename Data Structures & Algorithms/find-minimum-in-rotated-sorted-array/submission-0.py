class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            print(nums[mid])

            if nums[l] > nums[mid]:
                r = mid
            elif nums[mid + 1] > nums[r]:
                l = mid + 1
            else:
                return nums[l] if nums[l] < nums[mid + 1] else nums[mid + 1]
        
        return nums[r]