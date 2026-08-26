class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap
        # a c t :
        #[0] * 26
        #[1,0,1,0,0,0]
        # ord(char) - ord(a)

        anagrams = {}

        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord("a")] += 1
            alpha = tuple(alpha)
            
            
            if alpha in anagrams:
                anagrams[alpha].append(string)
            else:
                anagrams[alpha] = [string]
        
        return list(anagrams.values())
        