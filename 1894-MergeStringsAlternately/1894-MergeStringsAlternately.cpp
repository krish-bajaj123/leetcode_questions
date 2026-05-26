// Last updated: 5/26/2026, 4:33:46 PM
class Solution {
public:
    std::string mergeAlternately(const std::string& word1, const std::string& word2) {
        std::string result;
        int i = 0, j = 0;
        int len1 = word1.length(), len2 = word2.length();

        // Alternate adding characters from word1 and word2
        while (i < len1 || j < len2) {
            if (i < len1) {
                result.push_back(word1[i++]);
            }
            if (j < len2) {
                result.push_back(word2[j++]);
            }
        }

        return result;
    }
};