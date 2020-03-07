# coding=utf-8
'''
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    
    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
    
    示例 1:
    
    输入: [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。
    示例 2:
    
    输入: [2,7,9,3,1]
    输出: 12
    解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
         偷窃到的最高金额 = 2 + 9 + 1 = 12 。
    [5,4,3,9,1]   5 + 9
    
    抢第三个房子，将数额与第一个房子相加。

    不抢第三个房子，保持现有最大数额。
    
        max((n1+n3), n2)
        mx (n2+n4)
        f(k) = max(f(k – 2) + A_kA k, f(k – 1))
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/house-robber
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 记录上一次的最大值及目前的最大值，交替轮换找最大值
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0  # 目前最大值
        max2 = 0  # 上一个最大值
        for i in nums:
            temp = max1
            max1 = max((max2 + i), max1)
            max2 = temp
        return max1


if __name__ == '__main__':
    print(Solution().rob([4, 3, 5, 9, 1]))
