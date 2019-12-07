# coding=utf-8
'''

    给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
    
    在杨辉三角中，每个数是它左上方和右上方的数的和。
    
    示例:
    
    输入: 3
    输出: [1,3,3,1]
    进阶：
    
    你可以优化你的算法到 O(k) 空间复杂度吗？
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/pascals-triangle-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 通过上一层的数据，计算出下一层数据
class Solution1(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        for i in range(rowIndex + 1):
            row_list = [1] * (i + 1)
            if i >= 2:
                for j in range(1, i):
                    row_list[j] = new_list[j - 1] + new_list[j]
            new_list = row_list
        return new_list


# 方法1中上一层的数据为多余占用的空间，可以使用数组自身，每一层给数组末尾添加数据1（数组前面插入比较慢），
# 然后倒叙遍历，下一层的第i个数据，等于上一层的数据i和i-1的和
class Solution2(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row_list = []
        for i in range(rowIndex + 1):
            row_list.append(1)
            for j in reversed(range(1, i)):
                row_list[j] = row_list[j] + row_list[j - 1]
        return row_list


# 杨辉三角是左右对称的，所以我们在方法2的基础上改进，只计算后半部分的值，前半部分的值通过对称值相等得到
class Solution3(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row_list = []
        for i in range(rowIndex + 1):
            row_list.append(1)
            # print(row_list)
            for j in reversed(range((i+1)/2, i)):
                row_list[j] = row_list[j] + row_list[j - 1]
            for j in range(0, (i+1)/2):
                row_list[j] = row_list[i-j]
            # print(row_list)
        return row_list


def main():
    solution = Solution3()
    print(solution.getRow(6))


if __name__ == '__main__':
    main()
