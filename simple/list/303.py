# coding=utf-8
'''
    给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
    
    示例：
    
    给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
    
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3
    说明:
    
    你可以假设数组不可变。
    会多次调用 sumRange 方法。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/range-sum-query-immutable
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

class NumArray:
    def __init__(self, nums: List[int]):
        self.list_nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.list_nums[i:j + 1])


if __name__ == '__main__':
    list_data = [0, 1, 0, 3, 12]
    num_arr = NumArray(list_data)
    print(num_arr.sumRange(0, 8))
