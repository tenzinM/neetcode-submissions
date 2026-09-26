class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a -> z []
            
            for c in s:
                count[ord(c) - ord("a")] += 1
        
            
            res[tuple(count)].append(s)

            
        return list(res.values())

        # time complexity = m*n*26 = m*n
        # m = length of strs list
        # n = length of each char in strs list


