# coding=utf-8
'''
    给定一个整数数组 nums，将该数组升序排列。
    
     
    
    示例 1：
    
    输入：[5,2,3,1]
    输出：[1,2,3,5]
    示例 2：
    
    输入：[5,1,1,2,0,0]
    输出：[0,0,1,1,2,5]
     
    
    提示：
    
    1 <= A.length <= 10000
    -50000 <= A[i] <= 50000
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/sort-an-array
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def sortArray(self, nums):
        # 冒泡
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


class Solution1:
    def sortArray(self, nums):
        # 选择
        for i in range(len(nums)):
            small_num = i
            for j in range(i, len(nums)):
                if nums[small_num] > nums[j]:
                    small_num = j
            nums[i], nums[small_num] = nums[small_num], nums[i]
        return nums


# 插入
class Solution2:
    def sortArray(self, nums):
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums


# 快排
class Solution3:
    def sortArray(self, nums):

        def quick_sort(arr, start, end):
            if start >= end:
                return arr
            zhong = arr[start]
            low = start
            high = end
            while start < end:
                while start < end and arr[end] >= zhong:
                    end -= 1
                arr[start] = arr[end]
                while start < end and arr[start] <= zhong:
                    start += 1
                arr[end] = arr[start]
            arr[end] = zhong
            quick_sort(arr, low, start - 1)
            quick_sort(arr, start + 1, high)

        quick_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    list_data = [-1, 2, -8, -10]
    print(Solution2().sortArray(list_data))
