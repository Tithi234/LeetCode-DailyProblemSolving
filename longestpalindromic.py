class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        start = 0
        max_len = 1

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand_from_center(i, i)
            l2, r2 = expand_from_center(i, i + 1)

            if r1 - l1 + 1 > max_len:
                start = l1
                max_len = r1 - l1 + 1
            if r2 - l2 + 1 > max_len:
                start = l2
                max_len = r2 - l2 + 1

        return s[start:start + max_len]


