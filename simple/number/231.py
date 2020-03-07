# coding=utf-8
'''
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
    
    示例 1:
    
    输入: 1
    输出: true
    解释: 20 = 1
    示例 2:
    
    输入: 16
    输出: true
    解释: 24 = 16
    示例 3:
    
    输入: 218
    输出: false
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/power-of-two
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number = 1
        while number <= n:
            if number == n:
                return True
            else:
                number *= 2
        return False


# 按位运算，2的幂在二进制中是有一个 1 后跟一些 0
class Solution1(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & (-n) == n


if __name__ == "__main__":
    print(Solution1().isPowerOfTwo(128))
