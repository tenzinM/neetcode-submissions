class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force solution : multiply every num and divide by nums[i]
        # Real Solution : using prefix and postfix idea

        # array   [1, 2, 4, 6]  # 1st and last element prefix n postfix is 1
        # prefix  [1, 1, 2, 8] 
        # postfix [48,24,6, 1]
        # Answer  [48,24,12,8] multiply prefix and postfix num[i]

        res = [1] * len(nums);
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix;
            #print(res)
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res;

    


            