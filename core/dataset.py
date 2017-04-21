import utils

class Dataset:

	def __init__(self, filepath):
		dataset = open(filepath)
		self.data = dataset.read()

		dataset = open(filepath)
		self.lines = dataset.readlines()
		self.preprocess()

	def preprocess(self):

		# Fix non-unicode chars
		self.lines = [line.decode('unicode_escape').encode('ascii', 'ignore') for line in self.lines]

		# Remove duplicates
		newlist = []
		for line in self.lines:
			if line not in newlist:
				newlist.append(line)
		self.lines = newlist

	def get_words(self):
		return self.words

	def get_lines(self):
		return self.lines