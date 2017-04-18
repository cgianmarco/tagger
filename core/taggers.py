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
		n_features = 5000
		n_topics = 20
		n_top_words = 5

		tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                max_features=n_features,
                                stop_words=stopwords.words('italian'))

		

		self.mf = tf_vectorizer.fit_transform(self.dataset.lines)

		from collections import Counter

		counter = Counter()

		for k, v in self.mf:
			counter[tf_vectorizer.get_params()[k[1]]] += v

		self.most_common = np.asarray([ word for word in counter.most_common(n_tags)])


		if save:
			with open("generated/tags.txt", "wb") as f:
				np.savetxt(f, self.most_common, fmt="%s")
		if mf:
			self.save_factorization_matrix()


	def save_factorization_matrix(self):
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
