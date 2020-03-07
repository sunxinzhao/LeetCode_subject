# coding=utf-8
'''
- 题⽬七 给⼩朋友出题 同事⼩明家⾥有幼⼉园⼤班⼩朋友，有时候⽼师布置家庭作业，
  ⽐如，需要家⻓给⼩朋友出30道20 以内的加减法，不允许重复，也就是加数、被加数、和、减数、被减数、差 
  都在区间 [0, 20)内，⽐ 如： 19 - 6 = 13 12 + 6 = 18 8 - 8 = 0 
  ⼩明是个程序员，⽐较爱折腾，打算写⼀个⼩⼯具来完成这样的⼯作，
  可惜⼩明能⼒有限，遇到了 不少困难，请你帮助⼩明完成该功能。 
  输⼊： N 表示题⽬数量； 输出：满⾜条件的K个加减法，K <= N
'''
import random


# 获取随机的加法
def add():
    a = random.randint(0, 19)
    b = random.randint(0, 19 - a)
    return a, b, a + b


# 获取随机的减法
def sub():
    a = random.randint(0, 19)
    b = random.randint(0, a)
    return a, b, a - b


def test(n):
    res_d = {0: [], 1: []}
    sig_d = {0: add, 1: sub}
    i = 0
    while i < n:
        sig = random.randint(0, 1)
        method = sig_d[sig]
        a, b, r = method()
        while [a, b, r] in res_d[sig] or [b, a, r] in res_d[sig]:
            a, b, r = method()
        res_d[sig].append([a, b, r])
        i += 1
    return res_d


if __name__ == '__main__':
    res_d = test(30)
    for key, value in res_d.items():
        sign = '-'
        if key == 0:
            sign = '+'
        for a, b, r in value:
            print(a, sign, b, '=', r)
