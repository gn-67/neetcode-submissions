class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate once through, keeping note of seen
        #a dict of dicts... we store each word and the value is the character count
        # if the characters match then we pair the keys
        # seen = {}
        # for word in strs:
        #     sword = str(sorted(word))
        #     if sword in seen:
        #         seen[sword].append(word) 
        #     else:
        #         seen[sword] = [word]

        # return list(seen.values())


        result = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1 #maps characters from 0-26 using ASCII values 
            
            result[tuple(count)].append(s)

        return list(result.values())



    






        
