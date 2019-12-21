# coding=utf-8
'''
    给定一个正整数，返回它在 Excel 表中相对应的列名称。
    
    例如，
    
        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB 
        ...
    示例 1:
    
    输入: 1
    输出: "A"
    示例 2:
    
    输入: 28
    输出: "AB"
    示例 3:
    
    输入: 701
    输出: "ZY"
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/excel-sheet-column-title
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        data_dict = {0: '', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K',
                     12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V',
                     23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
        div = n // 26
        mod = n % 26
        return_data = ''
        while div:
            print(div, mod)
            if mod == 0:
                div = div - 1
                mod = 26

            return_data = data_dict[mod] + return_data
            mod = div % 26
            div = div // 26
        return_data = data_dict[mod] + return_data
        return return_data


def main():
    print(Solution().convertToTitle(703))


if __name__ == '__main__':
    main()
