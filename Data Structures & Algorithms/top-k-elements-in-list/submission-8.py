class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #we can use a dict to store frequency counts of each element
        # then we can return the top k values by sorting

        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        
        items = count.items()
        result = sorted(items, key = lambda x : x[1], reverse = True)

        return [result[i][0] for i in range(k)]