#add each valeu to a dict with the value being the count
#return the highest k values
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        sfreq = sorted(freq.items(), key=lambda item: item[1])
        top = sfreq[-k:]
        L = [top[i][0] for i in range(k)]
        return L

        