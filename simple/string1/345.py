# coding=utf-8
'''
    编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
    
    示例 1:
    
    输入: "hello"
    输出: "holle"
    示例 2:
    
    输入: "leetcode"
    输出: "leotcede"
    说明:
    元音字母不包含字母"y"。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 双指针
class Solution:
    def reverseVowels(self, s: str) -> str:
        yuanying_data = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s) - 1
        s_list = list(s)
        while left < right:

            if s[left] not in yuanying_data:
                left += 1
            if s[right] not in yuanying_data:
                right -= 1
            if s[left] in yuanying_data and s[right] in yuanying_data:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return ''.join(s_list)


if __name__ == '__main__':
    pattern = "leetcode"
    print(Solution().reverseVowels(pattern))
