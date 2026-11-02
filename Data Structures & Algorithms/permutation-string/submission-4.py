class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # A permutation cannot fit inside a shorter string
        if len(s1) > len(s2):
            return False

        # Count characters in s1 and the first window of s2
        s1Count = {}
        s2Count = {}

        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        matches = 0

        # Count characters whose frequencies match
        for ch in s1Count:
            if s1Count[ch] == s2Count.get(ch, 0):
                matches += 1

        # FIX: Check the initial window
        if matches == len(s1Count):
            return True

        # Sliding window
        l = 0

        for r in range(len(s1), len(s2)):

            # Add right character
            ch = s2[r]
            s2Count[ch] = s2Count.get(ch, 0) + 1

            if ch in s1Count:

                if s1Count[ch] == s2Count[ch]:
                    matches += 1

                elif s1Count[ch] + 1 == s2Count[ch]:
                    matches -= 1

            # Remove left character
            ch = s2[l]
            s2Count[ch] -= 1

            if ch in s1Count:

                if s1Count[ch] == s2Count[ch]:
                    matches += 1

                elif s1Count[ch] - 1 == s2Count[ch]:
                    matches -= 1

            l += 1

            if matches == len(s1Count):
                return True

        return False