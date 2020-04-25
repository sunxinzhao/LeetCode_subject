# coding=utf-8
'''
    给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
    
    示例 1:
    
    输入: [3,0,1]
    输出: 2
    示例 2:
    
    输入: [9,6,4,2,3,5,7,0,1]
    输出: 8
    说明:
    你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/missing-number
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        data_list = [-1] * (len(nums) + 1)
        for i in nums:
            data_list[i] = i
        for j in range(1, len(nums)):
            if data_list[j] - data_list[j - 1] != 1:
                return data_list[j - 1] + 1
        return data_list[-2] + 1


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        list_sum = len(nums) * (len(nums) + 1) // 2
        return list_sum - nums_sum


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(Solution1().missingNumber(nums))
