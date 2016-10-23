# coding=utf8


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        r = {}
        ret = ""

        if numRows == 1:
            return s
        if numRows == 2:
            for k, v in enumerate(s):
                if k % 2 == 0:
                    ret += v
            for k, v in enumerate(s):
                if k % 2 == 1:
                    ret += v
            return ret

        for i in xrange(numRows):
            r[i] = []
        for k, v in enumerate(s):
            first_b = int(k / (numRows - 1))

            flag = first_b % 2

            second = int(k % (numRows - 1))
            if flag == 0:
                r[second].append(v)
            else:
                r[numRows - 1 - second].append(v)

        for i in r:
            for j in r[i]:
                ret += j
        return ret


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    print Solution().convert(s, 3)
