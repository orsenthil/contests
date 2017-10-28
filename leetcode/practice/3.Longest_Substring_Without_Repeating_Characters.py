class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = longest = 0
        lastSeen = dict()

        for i in range(len(s)):
            if s[i] in lastSeen and start <= lastSeen[s[i]]:
                start = lastSeen[s[i]] + 1
            else:
                longest = max(longest, i - start + 1)
            lastSeen[s[i]] = i
        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("a"))
    print(s.lengthOfLongestSubstring("ab"))
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("bbbbbbbb"))


