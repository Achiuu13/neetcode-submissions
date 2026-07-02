class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> dupMap;

        for(int num: nums){
            if(dupMap.find(num) == dupMap.end()){
                dupMap[num] = 1;
            }else{
                dupMap[num] += 1;
            }
        }

        for(auto& pair: dupMap){
            if(pair.second > 1){
                return true;
            }
        }
        return false;
    }
};
