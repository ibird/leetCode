#!/usr/bin/env python
import time


class Solution(object):
    # @profile
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
                palindrome = "%s%s%s" % (s1[i], palindrome, s2[i])

        return palindrome

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        """
        ns = []
        for i in xrange(len(s)):
            ns.append("_")
            ns.append(s[i])
        ns.append("_")
        """

        for i in xrange(len(s)):
            s1 = s[i::-1]
            s2 = s[i::]
            print "first:%s %s" % (s1, s2)
            palindrome = self.cmpTwoString(s1, s2)
            longest = palindrome if len(palindrome) > len(longest) else longest
            if i > 0:
                s1 = "_" + s[i::-1]
                s2 = "_" + s[i::]
                print "second:%s %s" % (s1, s2)
                palindrome = self.cmpTwoString(s1, s2)
                longest = palindrome if len(palindrome) > len(longest) else longest
        return "".join(longest.split('_'))


if __name__ == "__main__":
    beginTime = int(time.time() * 1000)
    s = "abb"
    # s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
    # s = "jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx"
    print Solution().longestPalindrome(s)
    endTime = int(time.time() * 1000)
    print "time used:%d" % (endTime - beginTime)
