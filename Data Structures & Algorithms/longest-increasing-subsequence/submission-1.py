class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #we can use a cache + backtracking approach
        #we can grab the length of strictly increasing subsequence for each index to the end
        #we have to check if the number is less than the number before

        dp = [1] * len(nums)
        #dp[1,4,2,3,2,2,1]


        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)




        