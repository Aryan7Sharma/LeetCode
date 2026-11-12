class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int up=1;
        int down=1;
        int longsubarray = 1;
        for(int i=1; i<nums.length; i++){
            longsubarray = Math.max(longsubarray, Math.max(up,down));
            if (nums[i]>nums[i-1]){
                down=1;
                up+=1;
            }else if(nums[i]<nums[i-1]){
                up=1;
                down+=1;
            }else{
                up=1;
                down=1;
            }
            longsubarray = Math.max(longsubarray, Math.max(up,down));
        }
        return longsubarray;
    }
}