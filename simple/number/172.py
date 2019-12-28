# coding=utf-8
'''
    给定一个整数 n，返回 n! 结果尾数中零的数量。
    
    示例 1:
    
    输入: 3
    输出: 0
    解释: 3! = 6, 尾数中没有零。
    示例 2:
    
    输入: 5
    输出: 1
    解释: 5! = 120, 尾数中有 1 个零.
    说明: 你算法的时间复杂度应为 O(log n) 。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        factorial = str(factorial)
        print(factorial)
        zero_num = 0
        for i in range(len(factorial)):

            if factorial[len(factorial) - i - 1] == '0':
                zero_num += 1
            else:
                break
        return zero_num


class Solution1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while (n > 0):
            count += n / 5      # 25 / 5 = 5
            n = n / 5
        return count


def main():
    print(Solution1().trailingZeroes(24))


if __name__ == '__main__':
    main()
