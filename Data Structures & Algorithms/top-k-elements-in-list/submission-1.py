class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)] 
        # [[], [], [], [], [], [], []] we are using bucket sort 

        for num in nums:
            count[num] = 1 + count.get(num, 0)
       # print(count) # {1:1,2:2,3:3}

        for num, c in count.items():
            freq[c].append(num)
       # print(freq) # [[],[1],[2],[3],[],[],[]]

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
        #        print(num); # 3 , 2
                res.append(num)
                if len(res)==k:
                    return res


