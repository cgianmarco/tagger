from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
from collections import OrderedDict




class Tagger(CountVectorizer):

	def __init__(self, config):
		self.tags = []
		super(Tagger, self).__init__(**config)


	def run(self, n_tags, docs, filename="", save=True, mf=True):
		
		self.n_tags = n_tags

		self.docterm = self.fit_transform(docs)

		self.cooccurrence = self.docterm.T * self.docterm

		self.tag2frequency = OrderedDict(sorted([(word, self.docterm.getcol(idx).sum()) for word, idx in self.vocabulary_.items()], key = lambda x: -x[1])[:n_tags])

		self.tags = self.tag2frequency.keys()

		self.index = dict([(word, id_word) for word, id_word in self.vocabulary_.items() if word in self.tags])


		if save:
			# save tags
			with open("generated/tags_" + filename + ".txt", "wb") as f:
				np.savetxt(f, self.tags, fmt="%s")
		# if mf:
		# 	# save factorization matrix
		# 	with open("generated/matrix_" + filename + ".txt", "wb") as f:
		# 		np.savetxt(f, self.docterm.todense()[:, :self.n_tags], fmt="%s")

		return True


	def get_tagged_elements(self):
		# return len(filter(lambda elem: elem != 0, np.sum(self.docterm.todense()[:, :self.n_tags], axis=1)))
		tagged_elements = 0
		checked_docs = []
		for k in self.docterm.todok().keys():
			if k[1] in self.index.values() and k[0] not in checked_docs:
				checked_docs.append(k[0])
				tagged_elements += 1
		return tagged_elements

