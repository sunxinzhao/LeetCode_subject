# 给定两个字符串 s 和 t，它们只包含小写字母。
#
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
#  请找出在 t 中被添加的字母。
#
#
#
#  示例:
#
#  输入：
# s = "abcd"
# t = "abcde"
#
# 输出：
# e
#
# 解释：
# 'e' 是那个被添加的字母。
#
#  Related Topics 位运算 哈希表
#  👍 153 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict, t_dict = {}, {}
        for s1 in s:
            s_dict[s1] = s_dict.get(s1, 0) + 1
        for t1 in t:
            t_dict[t1] = t_dict.get(t1, 0) + 1

        for key, value in t_dict.items():
            if s_dict.get(key, 0) != value:
                return key
        return ''


class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        for key, val in collections.Counter(t).items():
            if not s.count(key) == val:
                return key


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    ransom = 'abcd'
    magazine = 'abcde'
    print(Solution().findTheDifference(ransom, magazine))
