# coding=utf-8
'''
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
    
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
    
    示例 1:
    
    输入: [3,2,3]
    输出: 3
    示例 2:
    
    输入: [2,2,1,1,1,2,2]
    输出: 2
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/majority-element
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        find_list = []
        for i in range(len(nums) / 2 + 1):
            if nums[i] in find_list:
                continue
            else:
                find_list.append(nums[i])
            num_i = 0
            for j in range(i, len(nums)):
                # print("i:"+str(nums[i]))
                # print("j:"+str(nums[j]))
                # print(num_i)
                if nums[i] == nums[j]:
                    num_i += 1
                if num_i > (len(nums) / 2):
                    return nums[i]
        return None


class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_data = {}
        for i in nums:
            num_count = dict_data.get(i)
            if num_count:
                dict_data[i] = num_count + 1
            else:
                dict_data[i] = 1
        return max(dict_data.keys(), key=dict_data.get)


def main():
    list_data = [8, 8, 7, 7, 7]
    print(Solution1().majorityElement(list_data))


if __name__ == '__main__':
    main()
