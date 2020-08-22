# coding=utf-8
'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
            else:
                return nums2[len(nums2) // 2]
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
            else:
                return nums1[len(nums1) // 2]
        nums1_left = 0
        nums2_left = 0
        num1, num2 = 0, 0
        med_index = (len(nums1) + len(nums2)) // 2
        while (nums1_left + nums2_left) < med_index:
            if nums1[nums1_left] < nums2[nums2_left]:
                num1 = nums1[nums1_left]
                nums1_left += 1
            else:
                num1 = nums2[nums2_left]
                nums2_left += 1
        if med_index % 2 == 0:
            return (num1 + num2) / 2
        return num2



class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
            else:
                return nums2[len(nums2) // 2]
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
            else:
                return nums1[len(nums1) // 2]
        nums1_left = 0
        nums2_left = 0
        list_data = []
        med_index = (len(nums1) + len(nums2)) // 2
        while (nums1_left + nums2_left) <= med_index:
            if nums1[nums1_left] < nums2[nums2_left]:
                list_data.append(nums1[nums1_left])
                nums1_left += 1
            else:
                list_data.append(nums2[nums2_left])
                nums2_left += 1
        if med_index % 2 == 0:
            return (list_data[-1] + list_data[-2]) / 2
        return list_data[-1]


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [-2, -1]
    print(Solution().findMedianSortedArrays(nums1, nums2))
