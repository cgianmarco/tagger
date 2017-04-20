from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np



class Tagger(CountVectorizer):

	def __init__(self, dataset, config):
		self.tags = []
		self.dataset = dataset

		super(Tagger, self).__init__(**config)


	def run(self, filename, save=True, mf=True):

		self.docterm = self.fit_transform(self.dataset.lines)

		self.cooccurrence = self.docterm.T * self.docterm

		self.tag2frequency = self.vocabulary_

		self.tags = self.tag2frequency.keys()


		if save:
			# save tags
			with open("generated/tags_" + filename + ".txt", "wb") as f:
				np.savetxt(f, self.tags, fmt="%s")
		if mf:
			# save factorization matrix
			with open("generated/matrix_" + filename + ".txt", "wb") as f:
				np.savetxt(f, self.docterm.todense(), fmt="%s")


	def get_tagged_elements(self):
		return len(filter(lambda elem: elem != 0, np.sum(self.docterm.todense(), axis=1)))

