class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate once through, keeping note of seen
        #a dict of dicts... we store each word and the value is the character count
        # if the characters match then we pair the keys
        seen = {}
        result = []
        for word in strs:
            sword = str(sorted(word))
            if sword in seen:
                seen[sword].append(word) 
            else:
                seen[sword] = [word]

        return list(seen.values())

        
