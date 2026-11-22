class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # A rotated sorted array is just two sorted arrays
        # find the rotated point and divide in two arrays

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:
                if target in nums[l:mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target in nums[mid:r + 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
