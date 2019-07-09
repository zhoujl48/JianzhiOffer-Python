#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
# 
"""
Project JianzhiOffer-Python -- 面试题39: 数组中出现次数超过一半的数字

背景：无
要求：数组中有一个数字出现次数超过数组长度的一半，请找出这个数字
输入：[1, 2, 3, 2, 2, 2, 5, 4, 2]
输出：2

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-09 
"""

class Solution(object):

    def _partition(self, arr, st, ed):
        """原地划分，仅使用常熟级别额外空间
        """
        pivot = ed
        left, right = st, ed - 1
        while left <= right:
            while left <= right and arr[left] < arr[pivot]:
                left += 1
            while left <= right and arr[right] > arr[pivot]:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
        arr[left], arr[pivot] = arr[pivot], arr[left]
        return left

    def find_more_than_half(self, arr):
        """返回出现次数超过数组长度一半的数字
        等价于寻找中位数
        """
        n = len(arr)
        mid = n // 2
        st, ed = 0, n - 1
        pivot = self._partition(arr, st, ed)
        while pivot != mid:
            (st, ed) = (st, pivot - 1) if pivot > mid else (pivot + 1, ed)
            pivot = self._partition(arr, st, ed)
        return arr[pivot]

    def quick_sort(self, arr, a, b):
        """快速排序，非本题要求，仅用于测试
        """
        if a >= b:
            return
        pivot = self._partition(arr, a, b)
        self.quick_sort(arr, a, pivot - 1)
        self.quick_sort(arr, pivot + 1, b)


# 测试
if __name__ == '__main__':

    arr_list = [
        [1, 2, 3, 2, 2, 2, 5, 4, 2],
        [3, 1, 4, 1, 5, 9, 2, 6, 9, 3, 3, 9, 7, 0, 4, 1, 3],
        [1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6, 7, 8, 7, 9]
    ]
    s = Solution()
    for arr in arr_list:
        print(s.find_more_than_half(arr))
        s.quick_sort(arr, 0, len(arr) - 1)
        print(arr)