class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        
        nums.sort()
        
        for k in range(len(nums)-2):
            i = k+1
            j = len(nums) - 1
            
            while (i < j):
                if nums[i] + nums[j] < -nums[k]:
                    i += 1

                elif nums[i] + nums[j] > -nums[k]:
                    j -= 1
        
                else:
                    if [nums[k], nums[i], nums[j]] not in final:
                        final.append([nums[k], nums[i], nums[j]])

                    i += 1
        
        return final