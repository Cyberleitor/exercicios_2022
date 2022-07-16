import wordcloud

# I tried write this code using only the library WordCloud Do you want to know the reason? Just a challenge for myself, thinking that if I used more libraries this little project would be "easier".

words_to_ignore = ['a', 'A', 'an', 'An', 'to', 'me', 'each', 'Each', 'Me', 'To', 'at', 'so', 'So', 'At', 'and', 'And', 'the', 'The', 'or', 'Or', 'from', 'From', 'but', 'But', 'for', 'For', 'is', 'Is', 'are', 'Are', 'in', 'In', 'on', 'On', 'it', 'It', 'of', 'Of', 'as', 'As', 'with', 'With', 'at', 'At', 'be', 'Be', 'by', 'By', 'not', 'Not', 'all', 'All', 'which', 'Which', 'its', 'Its', 'did', 'Did', "'s", 'am', "I'm", "'re", 'no', 'No', "'t", 'nor', 'Nor', "isn't", "'ll", 'whom', 'Whom', 'then', 'Then']

lines_of_the_text = [] # List to put the lines of the text (each one in a space).
words_of_the_text = [] # List to separate the individual words of the text.
words_without_signals = [] # List to "clean" the "words_of_the_text" (the previous list still had some unwanted particles of writing).
dictionary_words = {} # Dictionary to store the counting of the presence of words in the text.

with open('the_raven_poem.txt', 'r') as poe_poem:
	for line in poe_poem:
        	lines_of_the_text.append(line.split())

for group_of_words in lines_of_the_text:
	for each_word in group_of_words:
		if each_word not in words_to_ignore:
			words_of_the_text.append(each_word)

for each_word in words_of_the_text:
	each_word = each_word.replace(',', '')
	each_word = each_word.replace(';', '')
	each_word = each_word.replace('‘', '')
	each_word = each_word.replace('’', '')
	each_word = each_word.replace('—', '')
	each_word = each_word.replace('”', '')
	each_word = each_word.replace('“', '')
	each_word = each_word.replace('.', '')
	each_word = each_word.replace('!', '')
	each_word = each_word.replace('?', '')
	each_word = each_word.replace("’s", '')
	each_word = each_word.replace('o’er', '')
	each_word = each_word.replace('’Tis', '')
	if each_word == '' or each_word.lower() == 'or' or each_word.lower() == 'if':
		del each_word
	else:
		words_without_signals.append(each_word.upper())
			
for each_word in words_without_signals:
    if each_word not in dictionary_words.keys():
        dictionary_words[each_word] = 1
    else:
        dictionary_words[each_word] += 1

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(dictionary_words)
cloud.to_file("myfile.jpg")

