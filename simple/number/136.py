# coding=utf-8
'''
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    
    说明：
    
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    
    示例 1:
    
    输入: [2,2,1]
    输出: 1
    示例 2:
    
    输入: [4,1,2,1,2]
    输出: 4
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/single-number
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        point_num = []
        for i in nums:
            if i not in point_num:
                point_num.append(i)
            else:
                point_num.remove(i)
        return point_num[0]


# 题目中说到要找的元素出现一次，其余的元素都出现两次
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


def main():
    solution = Solution1()
    print(solution.singleNumber([4, 1, 2, 1, 2]))


if __name__ == '__main__':
    main()
