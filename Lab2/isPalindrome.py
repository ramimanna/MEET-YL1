word = raw_input("Type a word:")
new_list = []
for element in word:
    new_list.append(element)
print new_list
if new_list == new_list[::-1]:
	print "Congratulations! This is a Palindrome"
else:
	print "Nah, not this one!"