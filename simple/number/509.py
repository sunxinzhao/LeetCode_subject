'''
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
 

提示：

0 ≤ N ≤ 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 递归
class Solution:
    def fib(self, N: int) -> int:

        def digui(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            return digui(n-1) + digui(n-2)

        return digui(N)


# 迭代
class Solution1:
    def fib(self, N: int) -> int:

        for j in [lambda x: i * x for i in range(4)]:

            print(j)
        i = 0
        a = 0
        b = 1
        while i < N:
            a, b = b, a + b
            i += 1
        return a


# 0, 1, 1, 2, 3, 5, 8, 13, 21
if __name__ == "__main__":
    number = 7
    print(Solution1().fib(number))
