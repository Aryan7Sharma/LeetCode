#include<iostream>    
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = size(nums);
        for(unsigned int i=0; i<n; i++){
            int currValue = nums[i];
            nums[i] = currValue*currValue;
        }
        sort(nums.begin(), nums.end()); // Sorting the vector
        return nums;
    }
};