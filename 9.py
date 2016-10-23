# coding=utf8

class Solution(object):
    def isPalindrome(self, s):
        """
        :type x: int
        :rtype: bool
        """
        s = str(s)
        lenNum = len(s)
        if lenNum % 2 == 0:
            halfLenNum = lenNum / 2
            for i in xrange(halfLenNum):
                if s[i] != s[lenNum - i - 1]:
                    return False
            return True
        else:
            halfLenNum = (lenNum - 1) / 2
            for i in xrange(halfLenNum):
                if s[i] != s[lenNum - i - 1]:
                    return False
            return True

