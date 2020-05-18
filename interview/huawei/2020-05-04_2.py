# coding=utf-8
'''
实现报文转义功能报文中如果出现0x0A,转义成为2个字节0x12 0x34,
如果出现0x0B,转义成为2个字节0XAB 0XCD其他报文字节保持不变


输入描述：

1输入的报文为16进制,输入报文长度不超过127，输入的报文第一个字节为报文长度,
第一个字节（报文长度）算正式报文的一部分，但是不参与转义
2输入的报文每个字节用空格隔开

输出描述：

1输出为转义后的报文,转义后的报文长度也不超过255，输出的报文第一个字节算正式报文的一部分,为转义后的报文长度

2输出的报文内容大都为大写的十六进制，输出报文为十六进制，前不带0x前缀

3输出的报文每个字节用空格隔开
样例：
输入： 8 1 2 3 4 5 6 A
输出： 9 1 2 3 4 5 6 12 34
'''


class Solution:
    def to16(self, get_data):
        str_data = ''
        for i in range(1, len(get_data)):
            if get_data[i] == "A":
                str_data = str_data + "12" + ' ' + "34" + ' '
            elif get_data[i] == "B":
                str_data = str_data + "AB" + ' ' + "CD" + ' '
            else:
                str_data = str_data + str(get_data[i]) + ' '
        str_data = str(hex(len(str_data.split(' ')) - 1)[2:]).upper() + ' ' + str_data
        return str_data


if __name__ == "__main__":
    array_data = ["8", "1", "B", "3", "4", "5", "6", "A", "B"]
    print(Solution().to16(array_data))
