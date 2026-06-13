#nums[i] = -(nums[j] + nums[k])
# -nums[i] = nums[j] + nums[k]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()


        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = -(nums[i])

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                    continue
                if nums[left] + nums[right] > target:
                    right -= 1
                    continue
                if nums[left] + nums[right] == target:
                    result.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1

            

            
        return list(result)
                
                

