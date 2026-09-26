class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t) we can use this COunter method as well

        if len(s) != len(t):
            return False
        
        countFirstStr = {}
        countSecondStr = {}

        for i in range(len(s)) :
            countFirstStr[s[i]] = 1 + countFirstStr.get(s[i], 0)
            countSecondStr[t[i]] = 1 + countSecondStr.get(t[i], 0)

        print(countFirstStr)

        for c in countFirstStr :
            if countFirstStr[c] != countSecondStr.get(c, 0):
                return False
        return True
        
        
        