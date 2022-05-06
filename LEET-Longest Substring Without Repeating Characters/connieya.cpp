class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> arr(256 , -1);
        int maxLen = 0 , start =  -1;
        for(int i = 0; i < s.length(); i++){
            if(arr[s[i]] > start){
                start = arr[s[i]];
            }
            arr[s[i]] = i;
            if(maxLen < i-start){
                maxLen = i-start;
            }
        }
        return maxLen;
    }
};