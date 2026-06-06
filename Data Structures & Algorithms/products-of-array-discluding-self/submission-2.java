class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int pre_prod = 1;
        int[] prefix = new int[n];
        for(int i = 0; i < n; i++){
            res[i] = pre_prod;
            pre_prod *= nums[i];
        }
        int post_prod = 1;
        int[] postfix = new int[n];
        for(int i = n-1; i >= 0; i--){
            res[i] *= post_prod;
            post_prod *= nums[i];
        }
        return res;
    }
}  
