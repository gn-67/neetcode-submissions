class Solution:
#maybe we keep track
    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i]))
            s += "_"
            s += strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        L = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            length = int(s[i:j]) #because J is the # and is not included
            L.append(s[j + 1 : j + 1 + length])
            
            i = j + length + 1
                
        return L
