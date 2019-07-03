#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题05: 替换空格

背景：无
要求：实现函数，将字符串中每个空格替换成"%20"。
输入："We are happy."
输出："We%20are%20happy."

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-03
"""
class Solution(object):
    def __init__(self):
        pass

    def substitute(self, arr):
        """替换空格
        要求：实现函数，将字符串中每个空格替换成"%20"。
        输入："We are happy."
        输出："We%20are%20happy."
        """
        cnt = 0
        for ch in arr:
            if ch == ' ':
                cnt += 1

        i = len(arr) - 1
        arr += [' '] * 2 * cnt
        j = len(arr) - 1
        while i >= 0:
            if arr[i] != ' ':
                arr[j] = arr[i]
                j -= 1
            else:
                arr[j - 2:j + 1] = ['%', '2', '0']
                j -= 3
            i -= 1

        return arr


# 测试
if __name__ == '__main__':

    s = Solution()

    string = 'We are happy.'
    arr = [ch for ch in string]
    print(string)
    print(''.join(s.substitute(arr)))

