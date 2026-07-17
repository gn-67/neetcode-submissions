class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we can use recursive backtracking to solve this
        # checking each valid decision until we've accumulated all of the correct solutions

        result = []

        def dfs(i, cur, total):
            #lets write out our base cases
            if total == target:
                result.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)



        dfs(0, [], 0)
        return result