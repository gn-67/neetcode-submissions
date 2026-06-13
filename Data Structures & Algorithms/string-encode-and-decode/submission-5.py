class Solution:
    #we need to encode the string from list with helpful information
    #we can pass on the length of string numerically and add a # at end to signify end
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word))
            result += "#"
            result += word
        print(result)
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            result.append(s[i + 1: i + length + 1])
            i = i + int(length) + 1
   

        return result


