class Solution(object):
    """
    def lengthOfLongestSubstring(self, s):
        total = []
        lenSubStra = 0
        for i, k in enumerate(s):
            if k not in total:
                total.append(k)
            else:
                lenStr = len(total)
                if lenStr > lenSubStra:
                    lenSubStra = lenStr
                total = []
                total.append(k)
        lastlenSubStra = len(total)

        total = []
        lenSubStrb = 0
        for i, k in enumerate(s[::-1]):
            if k not in total:
                total.append(k)
            else:
                lenStr = len(total)
                if lenStr > lenSubStrb:
                    lenSubStrb = lenStr
                total = []
                total.append(k)
        lastlenSubStrb = len(total)
        return max(lenSubStra, lastlenSubStra, lenSubStrb, lastlenSubStrb)
    """

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxNum = 0
        substr = ""
        strLen = len(s)
        clist = []
        for c in s:
            if c not in clist:
                clist.append(c)
        cNum = len(clist)
        for i, k in enumerate(s):
            substr = ""
            total = []
            for j in xrange(i, (cNum+i if cNum + i < strLen else strLen)):
                char = s[j]
                if char not in total:
                    total.append(char)
                    substr += char
                    strNum = len(substr)
                    if strNum > maxNum:
                        maxNum = strNum
                    if maxNum == cNum:
                        return maxNum
                else:
                    strNum = len(substr)
                    if strNum > maxNum:
                        maxNum = strNum
                    if maxNum == cNum:
                        return maxNum
                    break
        return (maxNum if maxNum > len(substr) else len(substr))


if __name__ == "__main__":
    s = 'pwwkew'
    print Solution().lengthOfLongestSubstring(s)
