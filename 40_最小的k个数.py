#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
# 
"""
Project JianzhiOffer-Python -- 面试题40: 最小的k个数

背景：无
要求：输入n个整数，找出其中最小的k个数
输入：[1, 2, 3, 2, 2, 2, 5, 4, 2], k = 2
输出：[1, 2], (不考虑顺序)

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-09 
"""

class Solution(object):

    def _partition(self, arr, st, ed):
        """常数级别空间的划分函数
        """
        pivot = ed
        left, right = st, ed - 1
        while left <= right:
            while left <= right and arr[left] < arr[pivot]:
                left += 1
            while left <= right and arr[pivot] < arr[right]:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
        arr[left], arr[pivot] = arr[pivot], arr[left]
        return left

    def top_k_partition(self, arr, k):
        """最小k个数(Partition思想，会改变原始数组)
        时间效率：O(N)
        """
        n = len(arr)
        if n < k:
            return
        st, ed = 0, n - 1
        pivot = self._partition(arr, st, ed)
        while pivot != k - 1:
            (st, ed) = (st, pivot - 1) if pivot > k - 1 else (pivot + 1, ed)
            pivot = self._partition(arr, st, ed)
        return arr[:k]


    def down_heap(self, arr, i):
        """从节点i开始向下调整使其符合堆的定义
        """
        n = len(arr)
        while i < n:
            i_left, i_right = i * 2  + 1, i * 2  + 2
            if i_left < n:
                i_child_max = i_left
                if i_right < n:
                    i_child_max = i_right if arr[i_right] > arr[i_left] else i_left
                if arr[i] < arr[i_child_max]:
                    arr[i], arr[i_child_max] = arr[i_child_max], arr[i]
                i = i_child_max
            else:
                return

    def heapify(self, arr):
        """自底向上建堆，时间复杂度O(N)
        """
        n = len(arr)
        for i in list(range(n))[::-1]:
            if (i * 2 + 1) < n:     # 有左孩子
                self.down_heap(arr, i)
        return arr

    def top_k_heap(self, arr, k):
        """最小k个数(最大堆思想，不改变原始数组，适用于大数据)
        时间效率：O(Nlogk)
        """
        max_heap_k = self.heapify(arr[:k])
        for num in arr[k:]:
            if num < max_heap_k[0]:
                max_heap_k[0] = num
                self.down_heap(max_heap_k, 0)
        return max_heap_k


# 测试
if __name__ == '__main__':
    from numpy.random import seed, randint
    seed(47)

    s = Solution()
    for _ in range(5):
        arr = randint(100, size=20)
        print(arr, end='\t')
        print(s.top_k_partition(arr.copy(), k=5), end='\t')
        print(s.top_k_heap(arr.copy(), k=5))
