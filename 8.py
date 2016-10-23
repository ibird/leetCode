# coding = utf8


class Solution(object):
    def myAtoi(self, str):
        MAXNUM = 2147483647
        MINNUM = -2147483648
        r = ""
        for k, v in enumerate(str):
            if v == " " and r == "":
                continue
            if v == "-" and r == "":
                r += v
                continue
            if v == "+" and r == "":
                r += v
                continue

            if v in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                r += v
            else:
                break

        r = 0 if r in ['', '-', '+'] else int(r)
        if r > MAXNUM:
            r = MAXNUM
        if r < MINNUM:
            r = MINNUM
        return r

if __name__ == "__main__":
    print Solution().myAtoi("-12321adas")
