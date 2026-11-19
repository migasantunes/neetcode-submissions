class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while r > l:
            mid = l + (r - l) // 2

            if nums[mid] > nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid + 1] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        
        return l if nums[l] == target else -1