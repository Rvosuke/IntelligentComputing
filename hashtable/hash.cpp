class Solution {
public:
	bool isAnagram(string s, string t) {
		int record[26] = {0};  // 重要的是这里，定义时为{}
		for (int i = 0; i < s.size(); i++) {
			record[s[i] - 'a']++;
		}
		for (int i = 0; i < t.size(); i++) {
			record[t[i] - 'a']--;
		}
		for (int i = 0; i < 26; i++) {
			if (record[i] != 0) {
				return false;
			}
		}
		return true;
	}

	vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
		unordered_set<int> result_set;
		unordered_set<int> nums_set(nums1.begin(), nums1.end());
		for (int num : nums2) {
			if (nums_set.find(num) != nums_set.end()) {
				result_set.insert(num);
			}
		}
		return vector<int>(result_set.begin(), result_set.end());
	}
};