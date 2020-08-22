'''
    给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

    说明：不要使用任何内置的库函数，如  sqrt。

    示例 1：

    输入：16
    输出：True
    示例 2：

    输入：14
    输出：False

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/valid-perfect-square
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 二分查找
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num < 2:
            return True
        lager = num
        less = 0
        mid = num // 2 + 1
        biaoshi = True
        while (biaoshi):
            if mid * mid == num:
                return True
            elif mid * mid > num:
                lager = mid
                mid = (lager + less) // 2
            elif mid * mid < num:
                less = mid
                mid = (lager + less) // 2
            if lager == mid or less == mid or lager == less:
                biaoshi = False
        return False


# 递归
class Solution1:
    def isPerfectSquare(self, num: int) -> bool:

        # leetcode submit region end(Prohibit modification and deletion)
        if num < 2:
            return True

        def is_sqrt(start, end, num):
            if start * start == num or end * end == num:
                return True
            if end - start > 1:
                if end * end > num > start * start:
                    return is_sqrt(start, (start + end) // 2, num) or is_sqrt((start + end) // 2, end, num)

            return False

        return is_sqrt(0, num, num)


if __name__ == "__main__":
    for num in range(101):
        # num = 27
        print(str(num) + ':' + str(Solution().isPerfectSquare(num)))
