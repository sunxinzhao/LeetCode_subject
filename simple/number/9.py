'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 <= x < 10:
            return True
        weishu = len(str(x))
        new_number = 0
        for i in range(weishu // 2):
            new_number = new_number * 10 + x % 10
            x = x // 10
        if weishu % 2 != 0:
            x = x // 10
        if x == new_number:
            return True
        return False
        #         if x < 0:
        #             return False
        #         shuzi = x
        #         new_number = 0
        #         kaiguan = True
        #         while(kaiguan):
        #             if x >= 10:
        #                 new_number = new_number * 10 + x % 10
        #                 x = x / 10
        #             else:
        #                 new_number = new_number * 10 + x % 10
        #                 kaiguan = False
        #         if new_number == shuzi:
        #             return True
        #         else:
        #             return False


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        shuzi = str(x)
        shuzi = shuzi[::-1]
        if shuzi == str(x):
            return True
        return False


if __name__ == '__main__':
    nums = 1121
    print(Solution1().isPalindrome(nums))
