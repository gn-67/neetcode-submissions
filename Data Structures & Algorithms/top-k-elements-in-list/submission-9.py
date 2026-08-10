class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        values = list(sorted(count.items(), key = lambda i : i[1], reverse = True))

        result = []
        for i in range(k):
            result.append(values[i][0])

        return result
        