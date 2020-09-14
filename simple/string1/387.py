'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 示例：

 s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

 提示：你可以假定该字符串只包含小写字母。
 Related Topics 哈希表 字符串
'''

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


class Solution1:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        statistics_data = dict()
        for i in range(len(s)):
            if s[i] in statistics_data.keys():
                statistics_data[s[i]] = str((int(statistics_data[s[i]].split('_')[0]) + 1)) + '_' + \
                                        statistics_data[s[i]].split('_')[-1]
            else:
                statistics_data[s[i]] = str(1) + '_' + str(i)
        print(statistics_data)
        for key, value in statistics_data.items():
            if int(value.split('_')[0]) == 1:
                return int(value.split('_')[-1])
        return -1


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        # 自己想的办法
        s = list(s)
        one_time = dict()
        gt_one_time = dict()
        for i in range(len(s)):
            if s[i] not in one_time.keys() and s[i] not in gt_one_time.keys():
                one_time[s[i]] = i
            elif s[i] in one_time.keys() and s[i] not in gt_one_time.keys():
                one_time.pop(s[i])
                gt_one_time[s[i]] = i
        print(one_time)
        if len(one_time) > 0:
            return list(one_time.values())[0]
        else:
            return -1


if __name__ == "__main__":
    s = 'dddccdbba'
    print(Solution().firstUniqChar(s))
