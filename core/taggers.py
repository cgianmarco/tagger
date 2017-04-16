from nltk import FreqDist, bigrams
import utils



class SingleWordTagger:

	def __init__(self, save=True):
		self.tags = []

	def run(self, words, n_tags, save=True):
		fdist_words = FreqDist(words)

		for k,v in fdist_words.most_common(n_tags):
			self.tags.append(k)
		self.tags.remove("---")

		if save:
			import numpy as np
			with open("generated/tags.txt", "wb") as f:
				np.savetxt(f, np.asarray(self.tags), fmt="%s")

	def get_tags(self):
		return self.tags



class DoubleWordTagger:

	def __init__(self, save=True):
		self.tags = []

	def run(self, words, n_tags, save=True):
		bgs = bigrams(words)
		fdist_bigrams = FreqDist(bgs)

		for k,v in fdist_bigrams.most_common(n_tags):
			self.tags.append(k)
		self.tags = utils.remove_separators(self.tags)

		if save:
			import numpy as np
			with open("generated/double_tags.txt", "wb") as f:
				np.savetxt(f, np.asarray(self.tags), delimiter="-", fmt="%s")

	def get_tags(self):
		return self.tags
