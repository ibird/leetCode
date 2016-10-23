# coding=utf8


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = "-" if x < 0 else ""
        if x == 0 or x > 2147483647 or x < -2147483648:
            return 0
        x = abs(x)

        while x:
            i = x % 10
            r += str(i)
            x = int(x / 10)

        r = int(r)
        if r > 2147483647 or r < -2147483648:
            return 0
        else:
            return r

if __name__ == "__main__":
    print Solution().reverse(123)
    print Solution().reverse(-123)
