# coding=utf-8
from datetime import datetime

'''
    问题：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    
    注意：给定 n 是一个正整数。

    示例 1：
        输入： 2
        输出： 2
        解释： 有两种方法可以爬到楼顶。
        1.  1 阶 + 1 阶
        2.  2 阶
        
    示例 2：
        输入： 3
        输出： 3
        解释： 有三种方法可以爬到楼顶。
        1.  1 阶 + 1 阶 + 1 阶
        2.  1 阶 + 2 阶
        3.  2 阶 + 1 阶
        
'''

'''
    递归
    如果我们要计算的n=10，每次只能走1或者2个台阶，要上到台阶10有两种方式，
    1是从第九层台阶爬一层，2是从8层台阶爬两层
    这样将10层台阶的问题转化为爬9层和爬8层台阶，以此类推
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return_data = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return return_data


'''
    递归优化
    在递归中会重复的计算，可以将计算的值存入字典，每次计算都去判断，
    如果字典中有这个值，就不计算，直接取值，如果没有，计算并将值放入到字典中
'''
dict_list = {}


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in dict_list.keys():
            return dict_list[n]
        else:
            return_data = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            dict_list[n] = return_data
            return return_data


'''
    动态规划
    前面递归使用的是自顶向下循环调用，当然也可以自下向上推算
    f(3) = f(2) + f(1)
    f(4) = f(3) + f(2)
    f(5) = f(4) + f(3)
    ...
    
'''


class Solution3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0

        a = 1
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a


def main(argv=None):
    start_time = datetime.now()
    climb_stairs1 = Solution()
    print(climb_stairs1.climbStairs(40))
    end_time = datetime.now()
    print(end_time - start_time)
    print('------')

    start_time = datetime.now()
    climb_stairs2 = Solution2()
    print(climb_stairs2.climbStairs(40))
    end_time = datetime.now()
    print(end_time - start_time)
    print('------')

    start_time = datetime.now()
    climb_stairs3 = Solution3()
    print(climb_stairs3.climbStairs(40))
    end_time = datetime.now()
    print(end_time - start_time)
    print('------')


if __name__ == '__main__':
    main()
