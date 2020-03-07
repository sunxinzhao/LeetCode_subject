# coding=utf-8
'''
    给定两个字符串 s 和 t，判断它们是否是同构的。
    
    如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
    
    所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
    
    示例 1:
    
    输入: s = "egg", t = "add"
    输出: true
    示例 2:
    
    输入: s = "foo", t = "bar"
    输出: false
    示例 3:
    
    输入: s = "paper", t = "title"
    输出: true
    说明:
    你可以假设 s 和 t 具有相同的长度。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/isomorphic-strings
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_data = {}
        for i in range(len(s)):
            if s[i] not in dict_data.keys() and t[i] not in dict_data.values():
                dict_data[s[i]] = t[i]
            else:
                if s[i] in dict_data.keys() and t[i] != dict_data[s[i]]:
                    return False
                if t[i] in dict_data.values() and s[i] != list(dict_data.keys())[list(dict_data.values()).index(t[i])]:
                    return False
        return True


class Solution1(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_data = {}
        for i in range(len(s)):
            if s[i] not in dict_data.keys():
                if t[i] in dict_data.values():
                    return False
                else:
                    dict_data[s[i]] = t[i]
            else:
                if t[i] != dict_data[s[i]]:
                    return False
        return True


class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i, char in enumerate(s):
            if char not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[char] = t[i]
            else:
                if t[i] != dic[char]:
                    return False
        return True


if __name__ == '__main__':
    print(Solution1().isIsomorphic('abb', 'acc'))
