# reverse.py
s = input()
k = input()
k = int(k)

ans = ''
for i in range(0, len(s), 2*k):
	if i + k <= len(s):
		ans += s[i:i+k:-1]
		ans += s[i+k:i+2*k]
	else:
		ans += s[i::-1]

print(ans)