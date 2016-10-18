#!/usr/bin/env python


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenNums = len(nums1) + len(nums2)
        res = 0
        flag = lenNums % 2
        for i in xrange(lenNums):
            if (len(nums2) == 0) or (len(nums1) != 0 and nums1[0] < nums2[0]):
                small = nums1[0]
                nums1.pop(0)
            else:
                small = nums2[0]
                nums2.pop(0)
            if flag == 0:
                if i == (lenNums / 2 - 1) or i == (lenNums / 2):
                    res = res + small
            else:
                if i == int(lenNums / 2):
                    res = small
        if flag == 0:
            return float(res / 2.0)
        else:
            return res


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print Solution().findMedianSortedArrays(nums1, nums2)
    nums2 = [1, 2]
    nums1 = [3, 4]
    print Solution().findMedianSortedArrays(nums1, nums2)
