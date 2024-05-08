# import the array module
import numbers
import pprint


# Binary search function
def binary_search(ST: list, key: numbers):
    """
    在二分法中就体现了循环不变量的思想，即在整个算法编写过程中，采取一致的定义思路。
    我们在最开始设定为闭区间后，整个处理过程中就都是闭区间，不考虑任何开区间的问题
    :param ST:
    :param key:
    :return:
    """
    low = 0
    high = len(ST) - 1
    while low <= high:
        # find the middle index, defence against overflow
        middle = int(low + (high - low) / 2)
        if ST[middle] > key:
            high = middle - 1
        elif ST[middle] < key:
            low = middle + 1
        elif ST[middle] == key:
            return middle
        else:
            return False


# Delete the element in the ordered linear table
def delete_element_double_points(nums: list, val: int):
    """
    可以理解为让快指针不停向前探路，慢指针负责回收，目标值不可回收
    如果快指针没有发现目标值，就把当前值给慢指针，两个都往前走一步
    如果快指针发现了目标值，就让慢指针等一下。
    :param nums:
    :param val:
    :return:
    """
    slow_index = 0
    for fast_index in range(len(nums)):
        if nums[fast_index] != val:
            nums[slow_index] = nums[fast_index]
            slow_index += 1
    return nums[:slow_index], slow_index


def min_sub_array_len(s: int, nums: list):
    result = float('inf')
    for i in range(len(nums)):
        sums = 0
        for j in range(i, len(nums)):
            sums += nums[j]
            if sums >= s:
                sub_length = j - i + 1
                result = sub_length if sub_length < result else result
    return result if result != float('inf') else 0


def sliding_window(s: int, nums: list):
    result = float('inf')
    i = 0
    sums = 0
    for j in range(len(nums)):
        sums += nums[j]
        while sums >= s:
            sub_length = j - i + 1
            result = sub_length if sub_length < result else result
            sums -= nums[i]  # 这里可能会忽略掉
            i += 1
    return result if result != float('inf') else 0


def spira_matrix(n: int):
    res = [[0 for _ in range(n)] for _ in range(n)]
    startx, starty = 0, 0
    loop = n // 2
    mid = n // 2
    offset = 1
    count = 1

    while loop:
        i = startx
        j = starty
        for j in range(starty, starty + n - offset):
            res[i][j] = count
            count += 1
        j += 1
        for i in range(startx, startx + n - offset):
            res[i][j] = count
            count += 1
        i += 1
        for j in range(j, starty, -1):
            res[i][j] = count
            count += 1
        j -= 1
        for i in range(i, startx, -1):
            res[i][j] = count
            count += 1
        i -= 1

        startx += 1
        starty += 1
        offset += 2
        loop -= 1

    if n % 2:
        res[mid][mid] = count
    return res

