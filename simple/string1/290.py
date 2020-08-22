# coding=utf-8
'''
    给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
    
    这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
    
    示例1:
    
    输入: pattern = "abba", str = "dog cat cat dog"
    输出: true
    示例 2:
    
    输入:pattern = "abba", str = "dog cat cat fish"
    输出: false
    示例 3:
    
    输入: pattern = "aaaa", str = "dog cat cat dog"
    输出: false
    示例 4:
    
    输入: pattern = "abba", str = "dog dog dog dog"
    输出: false
    说明:
    你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。  
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/word-pattern
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dict_list = {}
        pattern = list(pattern)
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict_list.keys() and str[i] not in dict_list.values():
                dict_list[pattern[i]] = str[i]
            else:
                if (pattern[i] in dict_list.keys() and dict_list[pattern[i]] != str[i]) or (
                                str[i] in dict_list.values() and list(dict_list.keys())[
                            list(dict_list.values()).index(str[i])] != pattern[i]):
                    return False
        return True


class Solution2:
    def wordPattern(self, pattern: str, str: str) -> bool:
        print(set(zip(list(pattern), str.split(" "))))
        return len(set(pattern)) == len(set(zip(list(pattern), str.split(" ")))) == len(set(str.split(' ')))


if __name__ == '__main__':
    pattern = "abba"
    str_data = "dog cat cat dog"
    print(Solution2().wordPattern(pattern, str_data))
