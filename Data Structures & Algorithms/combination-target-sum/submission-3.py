class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #we can use a backtracking approach, where we keep adding the same integer to itself before expanding on to the nex one
        #we can maintain a pointer

        result = []

        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            

            cur.append(nums[i])

            dfs(i, cur, total + nums[i])
            cur.remove(nums[i])
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return result
        