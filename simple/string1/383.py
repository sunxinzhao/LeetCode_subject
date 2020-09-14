'''给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面
的字符构成。如果可以构成，返回 true ；否则返回 false。

 (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

 注意：

 你可以假设两个字符串均只含有小写字母。

 canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

 Related Topics 字符串
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_dict, mag_dict = {}, {}
        for ran in ransomNote:
            ran_dict[ran] = ran_dict.get(ran, 0) + 1
        for mag in magazine:
            mag_dict[mag] = mag_dict.get(mag, 0) + 1

        for key, value in ran_dict.items():
            # if mag_dict.get(key, 0) < value:
            if key not in mag_dict.keys() or value > mag_dict[key]:
                return False
        return True


if __name__ == '__main__':
    ransom = 'a'
    magazine = 'b'
    print(Solution().canConstruct(ransom, magazine))
