# coding=utf-8
'''
    给定一个整数，写一个函数来判断它是否是 3 的幂次方。
    
    示例 1:
    
    输入: 27
    输出: true
    示例 2:
    
    输入: 0
    输出: false
    示例 3:
    
    输入: 9
    输出: true
    示例 4:
    
    输入: 45
    输出: false
    进阶：
    你能不使用循环或者递归来完成本题吗？
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/power-of-three
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 3:
            print(n)
            n = n / 3

        return n == 3


class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        res = math.log10(n) / math.log10(3)
        print(res)
        return res - int(res) == 0


class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 1162261467 % n == 0


if __name__ == '__main__':
    print(Solution1().isPowerOfThree(387420481))
