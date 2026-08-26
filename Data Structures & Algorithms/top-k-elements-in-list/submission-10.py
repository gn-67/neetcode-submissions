class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap 

        frequencies = {}

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        

        sortFreq = list(sorted(frequencies.items(), key = lambda x : x[1], reverse = True))
        
        result = []
        for i in range(k):
            result.append(sortFreq[i][0])

        return result


        