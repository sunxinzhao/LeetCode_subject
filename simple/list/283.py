# coding=utf-8
'''
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    
    示例:
    
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]
    说明:
    
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/move-zeroes
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)):
                    if nums[j] != 0:
                        nums[j], nums[i] = nums[i], nums[j]
                        break
        print(nums)


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 找不为0的值
        b = 0        # 当前不为0的下一位
        for i in nums:
            if i != 0:
                nums[b] = i
                b += 1
        for j in range(b, len(nums)):
            nums[j] = 0
        print(nums)

if __name__ == '__main__':
    list_data = [0,1,0,3,12]
    Solution1().moveZeroes(list_data)