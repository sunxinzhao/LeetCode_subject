# coding=utf-8
'''

- 题⽬⼀ 部⻔调整优化 某公司内有 4 个项⽬组，项⽬组 A、B、C、D，项⽬组A现有10⼈，
    项⽬组B现有7⼈，项⽬组C现 有5⼈，项⽬组D现有4⼈。
    为了实现跨项⽬组协作，公司决定每⽉从⼈数最多的项⽬组中抽调 3 ⼈ 出来，
    到其他剩下 3 组中，每组 1 ⼈，这称之为⼀次调整优化（亦即经过第⼀次调整后，A组有7 ⼈，
    B组有8⼈，C组有6⼈，D组有5⼈）。那么请问，经过⼗年的优化调整后，各项⽬组各有⼏⼈？ 
    编程求解该问题。 
'''


class Solution(object):
    def person_num(self, times):
        list = [{'A': 7, 'C': 6, 'B': 8, 'D': 5}, {'A': 8, 'C': 7, 'B': 5, 'D': 6}, {'A': 5, 'C': 8, 'B': 6, 'D': 7},
                {'A': 6, 'C': 5, 'B': 7, 'D': 8}]
        return list[times % 4]

        times = times
        A_num = 10
        B_num = 7
        C_num = 5
        D_num = 4
        data_list = []
        for i in range(times + 1):
            max_num = max(A_num, B_num, C_num, D_num)
            if max_num == A_num:
                A_num -= 3
                B_num += 1
                C_num += 1
                D_num += 1
            elif max_num == B_num:
                A_num += 1
                B_num -= 3
                C_num += 1
                D_num += 1
            elif max_num == C_num:
                A_num += 1
                B_num += 1
                C_num -= 3
                D_num += 1
            elif max_num == D_num:
                A_num += 1
                B_num += 1
                C_num += 1
                D_num -= 3
            data_list.append({"A": A_num, "B": B_num, "C": C_num, "D": D_num})
            print({"A": A_num, "B": B_num, "C": C_num, "D": D_num})
        return {"A": A_num, "B": B_num, "C": C_num, "D": D_num}


if __name__ == '__main__':
    print(Solution().countPrimes(120))

''' A     B      C     D
    10    7      5     4
    7     8      6     5
    8     5      7     6
    5     6      8     7
    6     7      5     8
    7     8      6     5
'''
