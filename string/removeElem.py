def removeElement(nums, val):
    slow = 0
    for fast in nums:
        if fast != val:
            nums[slow] = fast
            slow += 1
    return nums

nums = [1, 2, 2, 5]
val = 2
print(removeElement(nums, val))