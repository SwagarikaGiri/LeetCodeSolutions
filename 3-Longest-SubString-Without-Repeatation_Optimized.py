class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexes = {}
        offset = 0
        longest = 0

        for i in range(0,len(s)):
            char_ = s[i]
            index = indexes.get(char_)
            if (index != None) and (index >= offset):
                length = i - offset
                offset = index + 1
                if length > longest:
                    longest = length
            indexes[char_] =i
        return max(longest, len(s)-offset)