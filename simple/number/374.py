'''
我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

 -1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！




示例 :

输入: n = 10, pick = 6
输出: 6
Related Topics 二分查找
'''


class Solution:
    def guessNumber(self, n: int) -> int:

        def find(start, end):
            mid = (start + end) // 2
            result_data = guess(mid)
            if result_data == 0:
                return mid
            elif result_data > 0:
                if end - start == 1:
                    return end
                start = mid
                return find(start, end)
            else:
                if end - start == 1:
                    return start
                end = mid
                return find(start, end)
        return find(0, n)


def guess(num: int):
    # my_num = randomInt(num)
    # print(my_num)
    if num == 1:
        return 0
    if num > 1:
        return -1
    if num < 1:
        return 1


if __name__ == "__main__":
    num = 1
    print(Solution().guessNumber(num))
