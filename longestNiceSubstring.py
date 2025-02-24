class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return ""

        char_set = set(s)
    
        for i, char in enumerate(s):
            if char.swapcase() not in char_set:
                left = longestNiceSubstring(s[:i])
                right = longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
    
        return s