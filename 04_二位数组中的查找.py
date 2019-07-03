#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 ***.com, Inc. All Rights Reserved
# The Common Tools Project
"""
Project JianzhiOffer-Python -- 面试题04: 二位数组中的查找

背景：在一个二位数组中，从左至右/从上到下均递增。
要求：判断二位数组中是否包含某数。
输入：num = 7
     matrix = [[ 1,  2,  8,  9],
               [ 2,  4,  9, 12],
               [ 4,  7, 10, 13],
               [ 6,  8, 11, 15]]
输出：True


Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-02 
"""

class Solution(object):
    def __init__(self):
        pass

    def find(self, matrix, num):
        """二维有序数组查找
        背景：在一个二位数组中，从左至右/从上到下均递增。
        要求：判断二位数组中是否包含某数。
        输入：num = 7
             matrix = [[ 1,  2,  8,  9],
                       [ 2,  4,  9, 12],
                       [ 4,  7, 10, 13],
                       [ 6,  8, 11, 15]]
        输出：True
        """
        n_row, n_col = len(matrix), len(matrix[0])
        i, j = 0, n_col - 1
        while 0 <= i < n_row and  0 <= j < n_col:
            if matrix[i][j] == num:
                return True
            if matrix[i][j] < num:
                i += 1
            else:
                j -= 1
        return False


# 测试
if __name__ == '__main__':

    s = Solution()

    matrix = [[1, 2,  8,  9],
              [2, 4,  9, 12],
              [4, 7, 10, 13],
              [6, 8, 11, 15]]
    for item in matrix:
        print(item)
    for num in range(5):
        print(num, s.find(matrix, num))

