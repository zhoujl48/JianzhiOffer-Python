#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题17: 打印从1到最大的n位数

背景：无
要求：从1开始打印到最大的n位数
输入：32
输出：1, 2, ..., 999

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-11
"""
class Solution(object):
    def __init__(self):
        pass

    def _recurse(self, res_num, res_digits):
        if not res_digits:
            for i in range(len(res_num)):
                if res_num[i] != '0':
                    print(res_num[i:], end=' ')
                    break
            return
        for i in range(10):
            self._recurse(res_num + str(i), res_digits - 1)

    def print_1_to_digit_n(self, n):
        """相当于数字数组全排列问题
        """
        self._recurse('', n)
        print()


# 测试
if __name__ == '__main__':

    s = Solution()
    s.print_1_to_digit_n(3)


