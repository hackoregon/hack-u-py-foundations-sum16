from pprint import prettyprint
word_dict = {}

with open('zen.txt','r') as f:
	words = f.read().split()
	print words


for word in words:
	if word in word_dict:
		word_dict[word] += 1
	else:
		word_dict[word] = 1
pprint.print(word_dict)