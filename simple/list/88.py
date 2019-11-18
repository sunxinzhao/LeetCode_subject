# coding=utf-8
'''
    问题：给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

    说明:
        初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
        
    示例:
        输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
        
        输出: [1,2,2,3,5,6] 
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n < 1:
            return nums1
        n_index = n - 1
        m_index = m - 1
        m_last = len(nums1) - 1
        while(n_index>=0):
            if m_index < 0:
                # 如果nums1提前结束，则将nums2中从头到n_index+1的值复制到对应的nums1上
                for i in range(n_index+1):
                    nums1[i] = nums2[i]
                return nums1
            if nums2[n_index] >= nums1[m_index]:
                nums1[m_last] = nums2[n_index]
                n_index = n_index - 1
            else:
                nums1[m_last] = nums1[m_index]
                m_index = m_index - 1
            m_last = m_last - 1
        return nums1

        # for i in range(n):
        #     nums1[i + m] = nums2[i]
        # nums1 = nums1[:m] + nums2
        # return list.sort(nums1)


def main():
    solution = Solution()
    data_list = solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(data_list)


if __name__ == '__main__':
    main()
