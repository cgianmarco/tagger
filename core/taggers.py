from nltk import FreqDist, bigrams
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import utils
import numpy as np
from nltk.corpus import stopwords



class SingleWordTagger:

	def __init__(self, dataset, save=True):
		self.tags = []
		self.dataset = dataset

	def run(self, n_tags, save=True, mf=True):

		tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                max_features=n_tags, token_pattern='(?u)\\b\\w+\\b',
                                stop_words=stopwords.words('italian'))		

		vectorized = tf_vectorizer.fit_transform(self.dataset.lines)

		self.mf = vectorized.todense()
		self.tags = tf_vectorizer.vocabulary_


		if save:
			# save tags
			with open("generated/tags.txt", "wb") as f:
				np.savetxt(f, self.tags.keys(), fmt="%s")
		if mf:
			# save factorization matrix
			with open("generated/matrix.txt", "wb") as f:
				np.savetxt(f, self.mf, fmt="%s")
		



class DoubleWordTagger:

	def __init__(self, dataset, save=True):
		self.tags = []
		self.dataset = dataset

	def run(self, n_tags, save=True):
		bgs = bigrams(self.dataset.words)
		fdist_bigrams = FreqDist(bgs)

		for k,v in fdist_bigrams.most_common(n_tags):
			self.tags.append(k)
		self.tags = utils.remove_separators(self.tags)

		if save:
			with open("generated/double_tags.txt", "wb") as f:
				np.savetxt(f, np.asarray(self.tags), delimiter="-", fmt="%s")

	def get_tags(self):
		return self.tags
