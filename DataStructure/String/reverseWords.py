# reverseWords.py
s = "   the sky is blue "

def erase_blank(s):
	fast = 0
	ans = []
	while fast < len(s) and s[fast] == ' ':
		fast += 1
	for i in range(fast, len(s)):
		if i + 1 < len(s) and s[i] == ' ' and s[i+1] == s[i]:
			continue
		else:
			ans.append(s[i])
	while len(ans) > 0 and ans[-1] == ' ':
		ans.pop(-1)
	return ''.join(ans)

def reverse_string(s):
	s = list(s)
	slow = 0
	fast = len(s) - 1
	while slow != fast and slow < fast:
		tmp = s[slow]
		s[slow] = s[fast]
		s[fast] = tmp
		slow += 1
		fast -= 1
	return ''.join(s)

def reverse_word(s):
	ans = ''
	s = erase_blank(s)
	s = reverse_string(s)
	j = 0
	for i, char in enumerate(s):
		if char == ' ':
			ans += reverse_string(s[j:i])
			ans += char
			j = i+1
	ans += reverse_string(s[j:])
	return ans

print(reverse_word(s))
