class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # we itrate through, we pick up the alpha frequency, we check if it exists
    # if it does, we add the word to the value array, if not we create the dict entry with the word in the value

        groups = {}

        for i in range(len(strs)):
            alpha = [0] * 26
            for j in range(len(strs[i])):
                alpha[ord(strs[i][j]) - ord('a')] += 1
            

            alpha = str(alpha)
            if alpha in groups:
                groups[alpha].append(strs[i])
            else:
                groups[alpha] = [strs[i]]
        
        return list(groups.values())


        