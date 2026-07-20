class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i<nums.length; i++){
            int count = 0;
            int a = nums[i];
            for (int j = 0; j < nums.length;j++){
                if (nums[j] == a){
                    count ++;
                }
            }
            if (count >= 2){
                return true;
            }
        }
        return false;
    }
}