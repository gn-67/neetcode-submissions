class Solution:
    def longestPalindrome(self, s: str) -> int:
        #maybe we use a hashmap to count
        #and return all the values that are even
        #pali can have only one odd in center

        count = collections.Counter(s)
        print(count)
        result = 0
        odds = 0

        for c in count.values():
            if c % 2 == 0:
                result += c
            else:
                if c - 1 > 0:
                    result += c - 1
                odds += 1
   
        if odds:
            odds = 1
        return result + odds





        

        