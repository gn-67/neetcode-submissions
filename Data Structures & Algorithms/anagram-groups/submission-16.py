class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we can use a hashset to keep track of character counts, thus grouping anagrams

        count = {}

        for i in range(len(strs)):
            alpha = [0] * 26
            for j in range(len(strs[i])):
                alpha[ord(strs[i][j]) - ord("a")] += 1
            chars = str(alpha)

            if chars in count:
                count[chars].append(strs[i])
            else:
                count[chars] = [strs[i]]
        
        return list(count.values())

        