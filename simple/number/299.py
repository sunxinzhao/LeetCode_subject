# coding=utf-8
'''
    你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，
    告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），
    有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。
    
    请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。
    
    请注意秘密数字和朋友的猜测数都可能含有重复数字。
    
    示例 1:
    
    输入: secret = "1807", guess = "7810"
    
    输出: "1A3B"
    
    解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
    示例 2:
    
    输入: secret = "1123", guess = "0111"
    
    输出: "1A1B"
    
    解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
    说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/bulls-and-cows
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


#
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        guess = list(guess)
        A_num = 0
        B_num = 0
        a_dict = {}
        b_dict = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A_num += 1
            else:
                if secret[i] in a_dict.keys():
                    a_dict[secret[i]] = a_dict[secret[i]] + 1
                else:
                    a_dict[secret[i]] = 1
                if guess[i] in b_dict.keys():
                    b_dict[guess[i]] = b_dict[guess[i]] + 1
                else:
                    b_dict[guess[i]] = 1
        for i in set(secret):
            if i in a_dict.keys() and i in b_dict.keys():
                B_num += min(a_dict[i], b_dict[i])
        return str(A_num) + 'A' + str(B_num) + 'B'


if __name__ == '__main__':
    A = '1123'
    B = '0111'
    print(Solution().getHint(A, B))
