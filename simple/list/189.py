# coding=utf-8
'''
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    
    示例 1:
    
    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
    示例 2:
    
    输入: [-1,-100,3,99] 和 k = 2
    输出: [3,99,-1,-100]
    解释: 
    向右旋转 1 步: [99,-1,-100,3]
    向右旋转 2 步: [3,99,-1,-100]
    
    说明:

    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的 原地 算法。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/rotate-array
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 输入: [1, 2, 3, 4, 5, 6, 7]和k = 3
        # 输出: [5, 6, 7, 1, 2, 3, 4]
        # 解释:
        # 向右旋转
        # 1步: [7, 1, 2, 3, 4, 5, 6]
        # 向右旋转
        # 2步: [6, 7, 1, 2, 3, 4, 5]
        # 向右旋转
        # 3步: [5, 6, 7, 1, 2, 3, 4]

        nums = nums[::-1]
        nums = nums[:k][::-1] + nums[k:][::-1]
        return nums
        # start_list = nums[-k:]
        # for i in range(len(nums) - 1, -1, -1):
        #     nums[i] = nums[i - k]
        # for i in range(len(start_list)):
        #     nums[i] = start_list[i]
        # return nums
        # for i in range(k):
        #     # 取出数组的最后一个值
        #     first = nums[-1]
        #     # 所以的数据向后移动一位
        #     for i in range(len(nums)-1, -1, -1):
        #         nums[i] = nums[i-1]
        #     nums[0] = first
        # return nums



def main():
    solution = Solution()
    print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))


if __name__ == '__main__':
    main()