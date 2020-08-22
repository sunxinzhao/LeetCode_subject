'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import math


# 我们做的最多的是将字符串反转，所以将数字x先转化成字符串A，将字符串进行反转成为字符串B，然后将字符串B转化成数字；
# 如果数字x是负数，则将符号单独取出，将去掉符号后的字符串A进行反转得到字符串B，将字符串B与符号拼接得到字符串C，然后将字符串C转化成数字；
class Solution:
    def reverse(self, x: int) -> int:
        shuzi = str(x)
        fuhao = ''
        if shuzi[:1] == '-':
            fuhao = '-'
            shuzi = shuzi[1:]
        shuzi = shuzi[::-1]
        shuzi = fuhao + shuzi
        if int(shuzi) >= math.pow(2, 31) or int(shuzi) < math.pow(-2, 31):
            return 0
        else:
            return int(shuzi)


if __name__ == '__main__':
    nums = -123
    print(Solution().reverse(nums))
