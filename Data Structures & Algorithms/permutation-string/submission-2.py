class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        countS1 = collections.Counter(s1)
        
        #could i just do a sliding window of size len(s1), create a counter of s2 at that window, compare it, and return true if htey are the same?
        #use a current counter, update it by deleting last char and adding new char on iteration

        countS2 = collections.Counter(s2[:len(s1) - 1])
        print(countS2)
        left = 0
        for right in range(len(s1) - 1, len(s2)):
            if s2[right] in countS2:
                countS2[s2[right]] += 1
            else:
                countS2[s2[right]] = 1

            print(countS2)

            if countS1 == countS2:
                return True

            if s2[left] in countS2:
                countS2[s2[left]] -= 1
            else:
                del countS2[s2[left]]

            left += 1

        return False