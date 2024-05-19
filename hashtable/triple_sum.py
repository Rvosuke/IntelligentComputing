# triple_sum.py
nums = input().split(" ")
nums = [int(num) for num in nums]

def threeSum(nums):
	hashmap = dict()
	for i, num1 in enumerate(nums):
		for j in range(i, len(nums)):
			sums = nums[i] + nums[j]
			if sums in hashmap:
				hashmap[sums].append([nums[i], nums[j]])
			else:
				hashmap[sums] = [[nums[i], nums[j]]]

	ans = []
	for i, num3 in enumerate(nums):
		if -num3 in hashmap:
			for l in hashmap[-num3]:
				if i not in l:
					l.append(i)
					ans.append(l)
	return ans

print(threeSum(nums))