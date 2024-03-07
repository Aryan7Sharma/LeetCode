#include <vector>
#include <algorithm>

class Solution {
public:
    int partitionDisjoint(std::vector<int>& nums) {
        int lMax = nums[0];
        int rMax = 0;
        int pos = 0;

        for (unsigned int i = 1; i < nums.size(); i++) {
            int currNum = nums[i];

            if (lMax > currNum) {
                pos = i;
                lMax = std::max(lMax, rMax);
                rMax = -1;
            } else{
                rMax = std::max(rMax, currNum);
            }
        }
        return pos+1;
    }
};
