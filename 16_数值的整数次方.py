#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题16: 数值的整数次方

背景：无
要求：实现pow(x, n)函数
输入：x
输出：x^n

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-11
"""
def swap_arr(arr, i, j):
    """交换数组元素
    """
    arr[i], arr[j] = arr[j], arr[i]


class Solution(object):
    def __init__(self):
        pass

    def my_pow(self, x, n):
        """快速幂方法
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        result = self.my_pow(x, n >> 1)
        result *= result
        if n & 1:
            result *= x
        return result



# 测试
if __name__ == '__main__':

    s = Solution()
    print(s.my_pow(2, 0))
    print(s.my_pow(2, 1))
    print(s.my_pow(2, 3))
    print(s.my_pow(2, 5))
    print(s.my_pow(3, 4))
    print(s.my_pow(3, 6))

