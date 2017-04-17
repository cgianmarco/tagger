from nltk.corpus import stopwords


def letters(input):
	text = []
	for c in input:
		if c.isalpha() or c == ' ':
			text.append(c)
		else:
			text.append(' ')
	return ''.join(text)


def no_stopwords(input):
	result = []
	for word in input:
		if word not in stopwords.words('italian'):
			result.append(word)
		else:
		   result.append('---')
	return result 


def remove_separators(bigrams):			
	return [ bigram for bigram in bigrams if "---" not in bigram ]
