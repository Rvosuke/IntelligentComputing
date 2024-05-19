from collections import Counter

# 四数相加2.py
while True:
	nums1 = input().split(" ")
	nums2 = input().split(" ")
	nums3 = input().split(" ")
	nums4 = input().split(" ")

	countAB = Counter(int(i) + int(j) for i in nums1 for j in nums2)
	counts = 0
	for num3 in nums3:
		for num4 in nums4:
			sums = int(num3) + int(num4)
			if -sums in countAB:
				counts += countAB[-sums]


	# counts = 0

	hashmap = dict()

	for i, num1 in enumerate(nums1.split(" ")):
		for j, num2 in enumerate(nums2.split(" ")):
			sums = int(num1) + int(num2)
			if sums not in hashmap:
				hashmap[sums] = [i, j]

	for k, num3 in enumerate(nums3.split(" ")):
		for l, num4 in enumerate(nums4.split(" ")):
			sums = int(num3) + int(num4)
			if -sums in hashmap:
				counts += 1

	# for num1 in nums1.split(" "):
	# 	for num2 in nums2.split(" "):
	# 		for num3 in nums3.split(" "):
	# 			for num4 in nums4.split(" "):
	# 				sums = int(num1) + int(num2) + int(num3) + int(num4)
	# 				if sums == 0:
	# 					counts += 1
	print(counts)