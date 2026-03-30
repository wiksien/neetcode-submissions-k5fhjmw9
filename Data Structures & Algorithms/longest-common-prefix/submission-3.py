class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        longest_common_pref = strs[0]

        for word in strs[1:]:
            temp_pref = ""
            for index, letter in enumerate(longest_common_pref):
                if index > len(word) - 1:
                    break
                if letter != word[index]:
                    break
                temp_pref += letter
            longest_common_pref = temp_pref

        return longest_common_pref