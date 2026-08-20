class Solution:
    #for this problem my first instinct is to iterate across each string in the list and append it to a result string
    #however I recognize that when decoding this string, our iteration needs to be able to know how long the current word is so it can append the correct amount of characters to each element in the output string


    def encode(self, strs: List[str]) -> str:

        result = ""

        for string in strs:
            result += str(len(string)) #since we are going to iterate, taking raw len(string) might cause us to overshoot but I will handle that once I have my core logic down
            result += "#"
            result += string
        
        print(result)
        return result


    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            length = ""
            string = ""

            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            result.append(s[i + 1:i + length + 1])
            #im not entirely sure if the indexes line up but once I finish coding up the solution, I will run some testcases through and then we can verify it togther, again I just want to get the core logic down
            i = i + length + 1
        return result


  



