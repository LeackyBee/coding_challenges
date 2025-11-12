from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Do this in reverse
        i = m + n - 1
        n1_p = m - 1
        n2_p = n - 1

        while n1_p >= 0 and n2_p >= 0:
            if nums1[n1_p] > nums2[n2_p]:
                nums1[i] = nums1[n1_p]
                n1_p -= 1
            else:
                nums1[i] = nums2[n2_p]
                n2_p -= 1
            i -= 1

        while n1_p >= 0:
            nums1[i] = nums1[n1_p]
            i -= 1
            n1_p -= 1

        while n2_p >= 0:
            nums1[i] = nums2[n2_p]
            i -= 1
            n2_p -= 1

