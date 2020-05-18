# coding=utf-8
'''
    文思海辉笔试题

    给定一个整数数组nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
    并返回他们的数组下标。你可以假设每种输入只会对应一个答案。
    但是，数组中同一个元素不能使用两遍。

    示例:给定nums = [2, 7, 11, 15], target = 9
    因为 nums[0]+ nums[1] = 2 + 7 = 9所以返回 [0, 1]
'''


# 双层循环
class Solution:
    def search(self, nums, target):
        if len(nums) < 2:
            return
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 字典
class Solution1:
    def search(self, nums, target):
        dict1 = {}
        for i in range(0, len(nums)):
            surplus_num = target - nums[i]
            if surplus_num not in dict1:
                dict1[nums[i]] = i
            else:
                return [dict1[surplus_num], i]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution1().search(nums, target))
