class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #when its a problem like this with an equation, we should try rearranging it to be easier to solve

        #here nums[i] = -(nums[j] + nums[k])
        #nums[j] + nums[k] = -nums[i]

        #we can also use a two pointer approach here to hit each value
        #and we can sort the original nums to iterate efficinetly and complete it in one pass

        numSort = sorted(nums)
        result = set()
        #so we do not add any duplicate triplets

        for i in range(len(numSort)):
            j = i + 1
            k = len(numSort) - 1

            while j < k:

                if numSort[j] + numSort[k] == -(numSort[i]):
                    result.add((numSort[i], numSort[j], numSort[k]))
                    j += 1

                
                elif numSort[j] + numSort[k] > -numSort[i]:
                    k -= 1


                
                elif numSort[j] + numSort[k] < -numSort[i]:
                    j += 1

        
        return list(result)
        