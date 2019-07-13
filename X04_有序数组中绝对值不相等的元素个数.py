#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 其它: 有序数组中绝对值不相等的元素个数

背景：无
要求：求有序数组中绝对值不相等的元素个数
输入：[-4, -2, -1, 0, 1, 1, 2, 3, 5]
输出：6

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-13
"""
class Solution(object):
    def __init__(self):
        pass

    def no_duplcated_abs(self, arr):
        st, ed = 0, len(arr) - 1
        cnt = 0
        while st <= ed:
            if abs(arr[st]) > abs(arr[ed]):
                st += 1
            elif abs(arr[st]) < abs(arr[ed]):
                ed -= 1
            else:
                st += 1
                ed -= 1
            cnt += 1
        return cnt


# 测试
if __name__ == '__main__':
    from numpy.random import choice, seed


    seed(0)
    s = Solution()
    for _ in range(5):
        nums = sorted(choice(list(range(-6, 10)), size=6, replace=False))
        print(nums, s.no_duplcated_abs(nums))

