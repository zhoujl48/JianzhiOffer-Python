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


def find_repeat_01(arr):
    """找出数组中任意一个重复数字
    背景：在一个长度为n的数组里的所有数字都在0～n-1范围内。数组中某些数字重复，但不知道重复数字和次数。
    要求：请找出数组中任意一个重复数字。
    输入：[2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3

    Args:
        arr: 输入数组

    Returns:
        若找出的重复数字，返回该数字
        若未找到，返回-1
    """
    if len(arr) in (0, 1):
        return -1

    for i in range(len(arr)):
        if i != arr[i]:
            if arr[i] == arr[arr[i]]:
                return arr[i]
            swap_arr(arr, i, arr[i])

    return -1


def find_repeat_02(arr):
    """不修改数组找出数组中任意一个重复数字
    背景：在一个长度为n+1的数组里的所有数字都在1～n范围内，故必存在重复数字。
    要求：不修改数组，找出重复数字
    输入：[2, 3, 5, 4, 3, 2, 6, 7]
    输出：2 或 3

    Args:
        arr: 输入数组

    Returns:
        重复数字
    """
    if len(arr) in (0, 1):
        return -1

    n = len(arr) - 1
    range_min = 1
    range_max = n
    while range_max - range_min > 0:
        mid = (range_min + range_max) // 2
        cnt_former = 0
        for num in arr:
            if num >= range_min and num <= mid:
                cnt_former += 1

        if range_max - range_min == 1:
            return range_min if cnt_former > mid - range_min + 1 else range_max

        if cnt_former > mid - range_min + 1:
            range_max = mid
        else:
            range_min = mid

    return range_min


if __name__ == '__main__':

    from numpy import random


    # a.
    # 测试重复数组
    print('a. 重复数组')
    random.seed(0)
    for _ in range(5):
        nums = random.choice(range(10), 10, replace=True)
        print(nums, find_repeat_01(nums))
    # 测试无重复数组
    print('a. 无重复数组')
    random.seed(0)
    for _ in range(5):
        nums = random.choice(range(10), 10, replace=False)
        print(nums, find_repeat_01(nums))


    # b.
    # 测试重复数组
    print('b. 重复数组')
    random.seed(0)
    for _ in range(5):
        nums = random.choice(range(1, 10), 10, replace=True)
        print(nums, find_repeat_02(nums))
