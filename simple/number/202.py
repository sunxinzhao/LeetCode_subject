# coding=utf-8
'''
    编写一个算法来判断一个数是不是“快乐数”。
    
    一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
    
    示例: 
    
    输入: 19
    输出: true
    解释: 
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/happy-number
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list_data = []
        while n != 1:
            num = 0  # 记录当前数按位平方和之后的值
            num1 = n   # 分解num1求和是的值
            while num1:
                num += (num1 % 10) * (num1 % 10)
                num1 = num1 / 10
            n = num
            print(n)
            if n not in list_data:
                list_data.append(n)
            else:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isHappy(999999999))
