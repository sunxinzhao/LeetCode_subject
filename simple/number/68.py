# coding=utf-8
'''
    实现 int sqrt(int x) 函数。
    
    计算并返回 x 的平方根，其中 x 是非负整数。
    
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
    
    示例 1:
    
    输入: 4
    输出: 2
    示例 2:
    
    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842..., 
         由于返回类型是整数，小数部分将被舍去。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/sqrtx
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(x):
            if x == i * i:
                return i
            if i * i < x < (i + 1) * (i + 1):
                return i


if __name__ == '__main__':
    print(Solution().mySqrt(2147395599))

    #
    # a = [1, 5, 7]
    # b = [1, 2, 3, 6, 8, 9, 10]
    # c = []
    # a1 = 0
    # b1 = 0
    # i = 0
    # while i < (len(a) + len(b)):
    #     if a1 < len(a) and b1 < len(b):
    #         while a1 < len(a) and b1 < len(b) and a[a1] <= b[b1]:
    #             c.append(a[a1])
    #             a1 += 1
    #             i += 1
    #         while a1 < len(a) and b1 < len(b) and b[b1] <= a[a1]:
    #             c.append(b[b1])
    #             b1 += 1
    #             i += 1
    #     else:
    #         if a1 >= len(a):
    #             while b1 < len(b):
    #                 c.append(b[b1])
    #                 b1 += 1
    #                 i += 1
    #         if b1 >= len(b):
    #             while a1 < len(a):
    #                 c.append(a[a1])
    #                 a1 += 1
    #                 i += 1
    #
    # print(c)
