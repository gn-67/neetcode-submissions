class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we want the characters in a given window to match the most common character in the given window
        # use hashmap to count occurrences 
        #take the length of the window and subtract from it the count of the most freq character
        # that returns the number of characters we want to replace
        # we check that that value is less than or equal to k
        # when this is true, our current window is valid
        # if the window is valid, shift right pointer
        # if window is invalid, shift left pointer up
        # result = r - l + 1

        left = 0
        count = {}
        result = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0) #returns a default value of 0 if get is not found
            length = right - left + 1

            while (right - left + 1) - max(count.values()) > k: #window invalid
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
            


        