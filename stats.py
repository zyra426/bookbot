def count_words(str):
	words = str.split()
	return len(words)


def count_char(str):
	char_count = {}
	char_list = []
	words = str.lower()

	for word in words:
		char_list.append(word)

	for char in char_list:
		if char in char_count:
			char_count[char] += 1
			continue

		char_count[char] = 1
	
	return char_count


def sort_on(items):
	return items["num"]


def sort_chars(chars):
	count_list = []
	char = {}
	
	for char in chars:
		char = {"char": char, "num": chars[char]}
		count_list.append(char)
	
	count_list.sort(reverse=True, key=sort_on)
	return count_list
