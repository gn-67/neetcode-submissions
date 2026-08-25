class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        cur = []

        def dfs(i):
            if i >= len(nums):
                result.append(cur.copy())
                return
            
            #we have two choices, we can add to our cur or we dont add to it
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
            dfs(i + 1)


            return
        
        dfs(0)
        return result
