# coding=utf-8
'''
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    
    示例 1:
    
    输入: s = "anagram", t = "nagaram"
    输出: true
    示例 2:
    
    输入: s = "rat", t = "car"
    输出: false
    说明:
    你可以假设字符串只包含小写字母。
    
    进阶:
    如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/valid-anagram
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 异位词:两个字符串中各字母的出现次数相同，则为异位词，否则不是异位词
import collections
import operator

# 对字符串根据字母排序，排序后的两个字符串相等就是异位词，不相等则不是异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)
        return operator.eq(dic1, dic2)


if __name__ == '__main__':
    s = 'anagram'
    t = 'nagaram'
    print(Solution1().isAnagram(s, t))
