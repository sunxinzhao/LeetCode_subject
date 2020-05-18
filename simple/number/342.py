# coding=utf-8
'''
    给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
    
    示例 1:
    
    输入: 16
    输出: true
    示例 2:
    
    输入: 5
    输出: false
    进阶：
    你能不使用循环或者递归来完成本题吗？
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/power-of-four
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 1:
            return False
        while num > 4:
            num = num / 4
        return num == 4


class Solution1:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        res = math.log10(num) / math.log10(4)
        return res - int(res) == 0


class Solution2:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        # print(math.pow(2, 31))
        # print(math.pow(4, 15))
        print([math.pow(4, i) for i in range(16)])
        return 1073741824 % num == 0


class Solution3:
    def isPowerOfFour(self, num: int) -> bool:
        list_data = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
        return num in list_data



if __name__ == '__main__':
    print(Solution3().isPowerOfFour(4))
    print(Solution2().isPowerOfFour(8))
    print(Solution2().isPowerOfFour(10))
    print(Solution2().isPowerOfFour(16))
    print(Solution2().isPowerOfFour(25))
    print(Solution2().isPowerOfFour(-16))
