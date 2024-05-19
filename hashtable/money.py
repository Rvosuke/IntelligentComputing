# money.py
import collections

ransomNote = input()
magazine = input()

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
	magazine_count = collections.Counter(magazine)
	for char in ransomNote:
		if char in magazine_count:
			magazine_count[char] -= 1
			if magazine_count[char] < 0:
				return False
		else:
			return False
	return True

print(canConstruct(ransomNote, magazine))