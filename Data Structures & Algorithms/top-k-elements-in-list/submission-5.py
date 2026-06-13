class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        scount = sorted(count.items(), key = lambda item : item[1], reverse = True)
        result = [scount[i][0] for i in range(k)]
        return result


#why do i use sorted instead of .sort here?