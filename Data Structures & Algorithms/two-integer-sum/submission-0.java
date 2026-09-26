class Solution {
    public int[] twoSum(int[] nums, int target) {
        //create a hashmap with keys (num) and value (index)
        HashMap<Integer, Integer> map = new HashMap<>();
        // loop through the nums 
        for(int i = 0; i< nums.length; i++) {
            //calculate the diff so to find the other num that added becomes target
            int diff = target - nums[i];
            if(map.containsKey(diff)) {
                return new int[]{map.get(diff), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}