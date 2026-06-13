class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we have to keep track of frequencies, which we can use an object for
        # then we can sort the items by frequencies and output the top k elements
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        top = sorted(freq.items(), key = lambda x : x[1], reverse = True)
        
        return [top[i][0] for i in range(k)]

        