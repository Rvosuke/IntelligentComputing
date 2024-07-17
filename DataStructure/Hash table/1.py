# hello world.py
while True:
	nums = input("Input the nums:")
	target = input("Input the target:")
	if not nums and not target:
		break
	nums = [int(num) for num in nums.split(" ")]
	target = int(target)
	hashtable = dict()
	for i, num in enumerate(nums):
		diff = target - num
		if diff in hashtable:
			print([i, hashtable[diff]])
			break
		else:
			hashtable[num] = i
