class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #when given an equation like this we can always start by thinking of rearranging the equation

        # nums[i] + nums[j] + nums[k] == 0
        # nums[i] = - (nums[j] + nums[k])
        # nums[j] + nums[k] = -nums[i]

        #so I'm thinking we can iterate over each index,
        #and while we iterate we can use a two pointer method to see if any two values sum to -nums[i],
        #if they do, we add it to our result

        result = set()
        sortNums = sorted(nums)


        for i in range(len(sortNums)):
            j = i + 1
            k = len(sortNums) - 1

            while j < k:
                if sortNums[j] + sortNums[k] == -(sortNums[i]):
                    result.add((sortNums[i], sortNums[j],sortNums[k]))
                    j += 1
                
                elif sortNums[j] + sortNums[k] > -(sortNums[i]):
                    #our number is over the target, we need to lower it
                    #oh our input isn't sorted, I;m going to sort it for implementation sake
                    k -= 1
                
                else:
                    j += 1
        
        return list(result)
        
        