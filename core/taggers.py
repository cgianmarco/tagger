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

		self.vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                max_features=n_tags, token_pattern='(?u)\\b\\w\\w\\w+\\b',
                                stop_words=stopwords.words('italian'))

		self.docterm = self.vectorizer.fit_transform(self.dataset.lines)

		self.cooccurrence = self.docterm.T * self.docterm

		self.tag2frequency = self.vectorizer.vocabulary_

		self.tags = self.tag2frequency.keys()


		if save:
			# save tags
			with open("generated/tags.txt", "wb") as f:
				np.savetxt(f, self.tags, fmt="%s")
		if mf:
			# save factorization matrix
			with open("generated/matrix.txt", "wb") as f:
				np.savetxt(f, self.docterm.todense(), fmt="%s")


	def get_tagged_elements(self):
		return len(filter(lambda elem: elem != 0, np.sum(self.docterm.todense(), axis=1)))
		



class DoubleWordTagger:

	def __init__(self, dataset, save=True):
		self.tags = []
		self.dataset = dataset

	def run(self, n_tags, save=True, mf=True):

		self.vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                max_features=n_tags, token_pattern='(?u)\\b\\w\\w\\w+\\b',
                                stop_words=stopwords.words('italian'), ngram_range=(2,2))

		self.docterm = self.vectorizer.fit_transform(self.dataset.lines)

		self.cooccurrence = self.docterm.T * self.docterm

		self.tag2frequency = self.vectorizer.vocabulary_

		self.tags = self.tag2frequency.keys()


		if save:
			# save tags
			with open("generated/double_tags.txt", "wb") as f:
				np.savetxt(f, self.tags, fmt="%s")
		if mf:
			# save factorization matrix
			with open("generated/double_matrix.txt", "wb") as f:
				np.savetxt(f, self.docterm.todense(), fmt="%s")

		# if save:
		# 	with open("generated/double_tags.txt", "wb") as f:
		# 		np.savetxt(f, np.asarray(self.tags), delimiter="-", fmt="%s")

	def get_tagged_elements(self):
		return len(filter(lambda elem: elem != 0, np.sum(self.docterm.todense(), axis=1)))

