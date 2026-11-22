class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2 # l + r // 2

            if nums[mid] < target:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        
        return -1 if nums[l] != target else l
            
