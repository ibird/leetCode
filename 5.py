#!/usr/bin/env python


class Solution(object):
    def cmpTwoString(self, s1, s2):
        lenStr = min(len(s1), len(s2))
        if lenStr > 0:
            palindrome = s1[0]
        else:
            return ""

        for i in xrange(1, lenStr):
            if s1[i] != s2[i]:
                break
            else:
                palindrome = s1[i] + palindrome + s2[i]

        return palindrome

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        ns = []
        for i in xrange(len(s)):
            ns.append("_")
            ns.append(s[i])
        ns.append("_")

        for i in xrange(len(ns)):
            s1 = ns[i::-1]
            s2 = ns[i::]
            palindrome = self.cmpTwoString(s1, s2)
            longest = palindrome if len(palindrome) > len(longest) else longest
        return "".join(longest.split('_'))


if __name__ == "__main__":
    s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
    print Solution().longestPalindrome(s)
