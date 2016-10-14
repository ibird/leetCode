class Solution(object):
    def calStr(self, s):
        t = []
        for i in s:
            if i not in t:
                t.append(i)
        return len(t)

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

    def alengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = []
        stringLen = len(s)
        for i, k in enumerate(s):
            if k not in total:
                total.append(k)
            for j in xrange(i + 1, stringLen):
                substr = s[i:j + 1]
                if len(substr) != self.calStr(substr):
                    break
                if substr not in total:
                    total.append(s[i:j + 1])
        a = 0
        for i in total:
            if len(i) > a:
                a = len(i)
        return a


if __name__ == "__main__":
    s = 'dvdf'
    print Solution().lengthOfLongestSubstring(s)
