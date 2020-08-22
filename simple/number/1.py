'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

from typing import List


# 暴力循环解答，遍历每个元素 x，并查找是否存在一个值与 x 相加等于target的目标元素。
# 时间复杂度 O(n^2)
# 空间复杂度 O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 使用空间换时间的方式解决问题，遍历一遍数组即可找到答案，
# 将当前数据和下标存放到字典中，在遍历的时候，判断target减去当前值的结果是不是在字典的键列表中，如果没有将当前数据和下标存放到字典中
# 如果存在，说明已经找到答案。返回当前数据的下标和字典中键对应的值。
'''
时间复杂度 O(n)
空间复杂度 O(n)
'''


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        in_dict = {}
        for i in range(len(nums)):
            if nums[i] in in_dict.keys():
                return [in_dict[nums[i]], i]
            else:
                in_dict[target - nums[i]] = i


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        in_dict = {}  # 存放当前值x和当前值的下标i的字典
        for i in range(len(nums)):
            if target - nums[i] in in_dict.keys():
                return [in_dict[target - nums[i]], i]
            else:
                in_dict[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution2().twoSum(nums, target))
