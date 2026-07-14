class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map <int, int> freq;
        for (int num : nums){
            freq[num]++;
        }
        int min = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (freq[nums[i]] == 1) 
            {
            return nums[i];
            }
        }
    }
};
