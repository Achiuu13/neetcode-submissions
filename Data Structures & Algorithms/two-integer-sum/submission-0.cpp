class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hashmap;
        for(int i = 0; i < nums.size();i++){
            int complement = target - nums[i];
            if(hashmap.find(complement) == hashmap.end()){
                hashmap[nums[i]] = i;
            }else{
                int j = hashmap[complement];
                vector<int>pair{j,i};
                return pair;
            }
        }
    }
};
