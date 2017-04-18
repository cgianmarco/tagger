from nltk import FreqDist, bigrams
import utils
import numpy as np



class SingleWordTagger:

	def __init__(self, dataset, save=True):
		self.tags = []
		self.dataset = dataset

	def run(self, n_tags, save=True, mf=True):
		fdist_words = FreqDist(self.dataset.words)

		for k,v in fdist_words.most_common(n_tags):
			self.tags.append(k)
		self.tags.remove("---")

		if save:
			with open("generated/tags.txt", "wb") as f:
				np.savetxt(f, np.asarray(self.tags), fmt="%s")
		if mf:
			self.generate_factorization_matrix()




	def generate_factorization_matrix(self):
		from collections import Counter

		# self.tags = ['collana', 'deck', 'pegasus', 'minnie', 'pokemon', 'carta']
		counter = Counter()

		for line in self.dataset.lines:
			found = []
			for word in line.split():
				if word in self.tags:
					found.append(word)
			for word in found:
				for word2 in found:
					counter[(word,word2)] += 1

		self.mf = np.array([[0 for x in self.tags] for y in self.tags])

		for i in range(len(self.tags)):
			for j in range(len(self.tags)):
				self.mf[i][j] = counter[(self.tags[i], self.tags[j])]

		with open("generated/matrix.txt", "wb") as f:
				np.savetxt(f, np.asarray(self.mf), fmt="%s")



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

