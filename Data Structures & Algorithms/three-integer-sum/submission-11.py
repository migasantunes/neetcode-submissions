class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        
        nums.sort()
        
        for k in range(len(nums)-2):
            if nums[k] > 0:
                break
            
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k+1
            j = len(nums) - 1
            
            while (i < j):
                currSum = nums[i] + nums[j]

                if currSum < -nums[k]:
                    i += 1

                elif currSum > -nums[k]:
                    j -= 1
        
                else:
                    final.append([nums[k], nums[i], nums[j]])

                    i += 1
                    j -= 1
                    
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                        
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

        return final