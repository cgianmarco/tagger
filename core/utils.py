from nltk.corpus import stopwords
import time

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


def time_usage(msg):
	def calc_time(func):
	    def wrapper(*args, **kwargs):
	    	print msg
	        beg_ts = time.time()
	        retval = func(*args, **kwargs)
	        end_ts = time.time()
	        print("Tempo impiegato: %f" % (end_ts - beg_ts))
	        return retval
	    return wrapper
	return calc_time



