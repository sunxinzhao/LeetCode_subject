'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
我们只需要循环遍历字符串中的每一个字符，将其转换为对应的数值相加即可得到结果。
由于I、X、C比较特殊
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
所以在遍历循环的时候判断当前字符是不是I、X、C，如果是，根据上述规则判断其后是不是对应的字符，如果是加上对应的值，
如果不是，则加本身所代表的值。
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        l = list(s)
        num = 0
        biaozhiwei = False
        for i in range(len(s)):
            if biaozhiwei:
                biaozhiwei = False
                continue
            if l[i] == 'I':
                if i + 1 < len(s) and l[i + 1] == 'V':
                    num = num + 4
                    biaozhiwei = True
                elif i + 1 < len(s) and l[i + 1] == 'X':
                    num = num + 9
                    biaozhiwei = True
                else:
                    num = num + 1
            if l[i] == 'X':
                if i + 1 < len(s) and l[i + 1] == 'L':
                    num = num + 40
                    biaozhiwei = True
                elif i + 1 < len(s) and l[i + 1] == 'C':
                    num = num + 90
                    biaozhiwei = True
                else:
                    num = num + 10
            if l[i] == 'C':
                if i + 1 < len(s) and l[i + 1] == 'D':
                    num = num + 400
                    biaozhiwei = True
                elif i + 1 < len(s) and l[i + 1] == 'M':
                    num = num + 900
                    biaozhiwei = True
                else:
                    num = num + 100
            if l[i] == 'V':
                num = num + 5
            if l[i] == 'L':
                num = num + 50
            if l[i] == 'D':
                num = num + 500
            if l[i] == 'M':
                num = num + 1000
        return num


'''
当小值在大值的左边，则减小值，如 IV=5-1=4；
当小值在大值的右边，则加小值，如 VI=5+1=6；
由上可知，右值永远为正，因此最后一位必然为正。
一言蔽之，把一个小值放在大值的左边，就是做减法，否则为加法。
在代码实现上，可以往后看多一位，对比当前位与后一位的大小关系，从而确定当前位是加还是减法。当没有下一位时，做加法即可。
也可保留当前位的值，当遍历到下一位的时，对比保留值与遍历位的大小关系，再确定保留值为加还是减。最后一位做加法即可。
'''

class Solution1:
    def romanToInt(self, s: str) -> int:
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                num = num - a[s[i]]
            else:
                num = num + a[s[i]]
        return num


if __name__ == '__main__':
    nums = "MCMXCIV"
    print(Solution1().romanToInt(nums))
