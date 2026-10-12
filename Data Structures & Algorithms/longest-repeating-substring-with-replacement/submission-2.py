class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hashmap to count the occurance of each character
        res = 0
        l=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k : 
                # (r - l + 1) represents the window length l->r
                # window length - count of max character > K
                # this condition says in this window the no. of character we need to replace
                # is more than the required K so we shift the left pointer and decrement the
                # count of left character and decrease the size of window
                count[s[l]] -= 1
                l+=1
            
            res = max(res, r - l + 1) # max length of valid window
        return res
        
        