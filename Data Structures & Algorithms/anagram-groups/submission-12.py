class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate through every element
        # we can create an empty array holding each letter, incrementing the specific letters
        # have that be the key, have the value be the actual word
        # then return an array of the values from the dict
        #use default dict in order to fill empty keys with list - allow us to use 
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            alpha = [0] * 26
            for j in range(len(strs[i])):
                char = ord(strs[i][j]) - ord('a')
                alpha[char] += 1
            
            anagrams[str(alpha)].append(strs[i])
        
        return list(anagrams.values())

        