class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #the target is 0
        #nums[i] == -(nums[j] + nums[k])
        #-nums[i] = nums[j] + nums[k]

        numSort = sorted(nums)
        print(numSort)
        result = set()

        for i in range(len(numSort)):


            target = -numSort[i]
            j = i + 1
            k = len(numSort) - 1



            while j < k:

                if numSort[j] + numSort[k] == target:
                    result.add(tuple([numSort[i], numSort[j], numSort[k]]))
                    j += 1
                    continue


                elif numSort[j] + numSort[k] > target:
                    k -= 1
                    continue
                
                else:
                    j += 1
        
        print(result)
        return list(result)






        