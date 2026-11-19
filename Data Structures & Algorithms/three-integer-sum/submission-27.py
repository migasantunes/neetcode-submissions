class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force would be a triple loop running nums O(n^3)

        # I'll do 3 pointers instead

        seen = set()
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    triple = (nums[i], nums[l], nums[r])
                    if triple not in seen:
                        res.append(list(triple))
                        seen.add(triple)
                    l += 1
                    r -= 1
        return res
