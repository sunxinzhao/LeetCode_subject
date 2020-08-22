'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import typing.List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ''
        min_len = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(min_len):
                min_len = strs[i]
        equ_str = ''
        for i in range(len(min_len)):
            for j in range(len(strs)):
                if min_len[i] != strs[j][i]:
                    return equ_str
            equ_str = equ_str + min_len[i]
        return equ_str


if __name__ == '__main__':
    nums1 = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(nums1))
