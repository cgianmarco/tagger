from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
from collections import OrderedDict
from utils import time_usage




class Tagger(CountVectorizer):


	def __init__(self, config):
		self.tags = []
		super(Tagger, self).__init__(**config)


	@time_usage("Running configuration...")
	def run(self, n_tags, docs, filename="", save=True):
		
		self.n_tags = n_tags

		self.docs = docs

		self.filename = filename

		self.docterm = self.calc_docterm()

		self.cooccurence = self.calc_cooccurence()

		self.tag2frequency = self.calc_tag2frequency()

		self.tags = self.calc_tags()

		self.index = self.calc_index()


		if save:
			self.save_tags()
			

		return True

	@time_usage("Calculating docterm...")
	def calc_docterm(self):
		return self.fit_transform(self.docs)

	@time_usage("Calculating cooccurrence...")
	def calc_cooccurence(self):
		return self.docterm.T * self.docterm

	@time_usage("Calculating tag2frequency...")
	def calc_tag2frequency(self):
		return OrderedDict(sorted([(word, self.docterm.getcol(idx).sum()) for word, idx in self.vocabulary_.items()], key = lambda x: -x[1])[:self.n_tags])

	@time_usage("Calculating tags...")
	def calc_tags(self):
		return self.tag2frequency.keys()

	@time_usage("Calculating index...")
	def calc_index(self):
		return dict([(word, id_word) for word, id_word in self.vocabulary_.items() if word in self.tags])

	@time_usage("Saving tags...")
	def save_tags(self):
		with open("generated/tags_" + self.filename + ".txt", "wb") as f:
				np.savetxt(f, self.tags, fmt="%s")

	@time_usage("Getting tagged elements")
	def get_tagged_elements(self):
		# return len(filter(lambda elem: elem != 0, np.sum(self.docterm.todense()[:, :self.n_tags], axis=1)))
		tagged_elements = 0
		checked_docs = []
		for k in self.docterm.todok().keys():
			if k[1] in self.index.values() and k[0] not in checked_docs:
				checked_docs.append(k[0])
				tagged_elements += 1
		return tagged_elements

