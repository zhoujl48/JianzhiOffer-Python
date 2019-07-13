#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
# 
"""
Project JianzhiOffer-Python -- 面试题48: 最长无重复子串

背景：无
要求：从字符串中找出最长的不包含重复字符的子字符串，并计算该最长子字符串的长度，假设只包含'a'~'z'
输入：arabcacfr
输出：acfr, 4

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-09 
"""

class Solution(object):

    def longest_substring_without_duplicatoin(self, string):
        """最长无重复子串(动态规划)
        """

        hashmap = lambda ch: ord(ch) - ord('a') # 将26个字母映射到长度为26的列表中，简单哈希
        position = [-1] * 26                    # 初始化所有字符的最大索引位置为-1，代表从未出现过
        position[hashmap(string[0])] = 0        # 第一个字符出现的最大索引初始化为0

        length = [0] * 26
        length[0] = 1
        lswd = string[0]
        for i in range(1, len(string)):
            ch = string[i]
            if position[hashmap(ch)] == -1:
                length[i] = length[i - 1] + 1
            else:
                d = i - position[hashmap(ch)]       # d为当前字符距上次出现位置的距离
                if d <= length[i - 1]:              # 若 距离d <= 以前一个字符为结尾的最大无重复子串长度length[i - 1]:
                    length[i] = d                   #   则 以当前字符为结尾的最大无重复子串长度length[i] 更新为 距离d
                else:                               # 若 距离d > 以前一个字符为结尾的最大无重复子串长度length[i - 1]:
                    length[i] = length[i - 1] + 1   #   则 以当前字符为结尾的最大无重复子串长度length[i] 直接等于 length[i - 1] + 1
            if len(lswd) < length[i]:
                lswd = string[i - length[i] + 1:i + 1]
            position[hashmap(string[i])] = i    # 更新当前字符的最大索引位置

        return lswd


# 测试
if __name__ == '__main__':

    from numpy.random import choice, seed

    s = Solution()
    seed(0)
    for _ in range(5):
        string = ''.join(choice(['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'], size=9, replace=True))
        lswd = s.longest_substring_without_duplicatoin(string)
        print('原始字符串：{}\t最长无重复子串：{}\t长度：{}'.format(string, lswd, len(lswd)))