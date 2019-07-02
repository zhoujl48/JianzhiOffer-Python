#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 ***.com, Inc. All Rights Reserved
# The Common Tools Project
"""
Project JianzhiOffer-Python -- 面试题03: 数组中重复的数字

a. 找出数组中重复数字
背景：在一个长度为n的数组里的所有数字都在0～n-1范围内。数组中某些数字重复，但不知道重复数字和次数。
要求：请找出数组中任意一个重复数字。
输入：[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

b. 不修改数组，找出数组中重复数字
背景：在一个长度为n+1的数组里的所有数字都在1～n范围内，故必存在重复数字。
要求：不修改数组，找出重复数字
输入：[2, 3, 5, 4, 3, 2, 6, 7]
输出：2 或 3

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-02 
"""
def swap_arr(arr, i, j):
    """交换数组元素
    """
    arr[i], arr[j] = arr[j], arr[i]


class Solution(object):
    def __init__(self):
        pass

    def find_repeat_01(self, arr):
        """找出数组中任意一个重复数字
        背景：在一个长度为n的数组里的所有数字都在0～n-1范围内。数组中某些数字重复，但不知道重复数字和次数。
        要求：请找出数组中任意一个重复数字。
        输入：[2, 3, 1, 0, 2, 5, 3]
        输出：2 或 3
        """
        if len(arr) in (0, 1):
            return -1

        for i in range(len(arr)):
            if i != arr[i]:
                if arr[i] == arr[arr[i]]:
                    return arr[i]
                swap_arr(arr, i, arr[i])

        return -1


    # 二分迭代
    def find_repeat_02_iter(self, arr):
        """不修改数组找出数组中任意一个重复数字
        背景：在一个长度为n+1的数组里的所有数字都在1～n范围内，故必存在重复数字。
        要求：不修改数组，找出重复数字
        输入：[2, 3, 5, 4, 3, 2, 6, 7]
        输出：2 或 3

        迭代法
        """
        if len(arr) in (0, 1):
            return -1

        st, ed = 1, len(arr) - 1
        while ed - st > 0:
            mid = (st + ed) // 2
            # 计算搜索区域内元素个数
            cnt_small = 0
            for num in arr:
                if st <= num <= mid:
                    cnt_small = cnt_small + 1
            # 更新搜索范围
            if cnt_small > mid - st + 1:
                ed = mid
            else:
                st = mid + 1

        return st

    # 二分递归
    def find_repeat_02_recurse(self, arr):
        """不修改数组找出数组中任意一个重复数字
        背景：在一个长度为n+1的数组里的所有数字都在1～n范围内，故必存在重复数字。
        要求：不修改数组，找出重复数字
        输入：[2, 3, 5, 4, 3, 2, 6, 7]
        输出：2 或 3

        递归法
        """
        if len(arr) in (0, 1):
            return -1

        st, ed = 1, len(arr) - 1
        return self._recurse(arr, st, ed)

    def _recurse(self, arr, st, ed):
        """递归调用，获取重复数字范围
        Args:
            arr: 被搜索的数组
            range_st: 搜索范围起点
            range_ed: 搜索范围终点
        """
        # 递归出口
        if ed == st:
            return st
        # 计算搜索区域内元素个数
        mid = (st + ed) // 2
        cnt_small = 0
        for num in arr:
            if st <= num <= mid:
                cnt_small = cnt_small + 1
        return self._recurse(arr, st, mid) if cnt_small > mid - st + 1 else self._recurse(arr, mid + 1, ed)


# 测试
if __name__ == '__main__':
    from numpy import random
    random.seed(0)

    s = Solution()
    # a. 测试重复数组
    print('a. 重复数组')
    for _ in range(5):
        nums = random.choice(range(10), 10, replace=True)
        print(nums, s.find_repeat_01(nums))
    # a. 测试无重复数组
    print('a. 无重复数组')
    for _ in range(5):
        nums = random.choice(range(10), 10, replace=False)
        print(nums, s.find_repeat_01(nums))
    # b. 测试重复数组
    print('b. 重复数组')
    for _ in range(5):
        nums = random.choice(range(1, 10), 10, replace=True)
        print(nums, s.find_repeat_02_iter(nums))
        print(nums, s.find_repeat_02_recurse(nums))
