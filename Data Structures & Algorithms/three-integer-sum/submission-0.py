class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() #sorting always takes nlogn time complexity

        for i, num in enumerate(nums):
            # Skip duplicate first numbers
            if i > 0 and num == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l<r:
                threeSum = num + nums[l] + nums[r]

                if threeSum > 0 :
                    r-=1
                elif threeSum < 0 :
                    l+=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    # Skip duplicate left values
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res

        #   1. Sort
        #       ↓
        #   2. Fix one number (i)
        #       ↓
        #   3. Two pointers: l = i+1, r = end
        #       ↓
        #   4. Compare sum:
        #   > 0 → r--
        #   < 0 → l++
        #  = 0 → save result + skip duplicates 
        