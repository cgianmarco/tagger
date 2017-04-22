from utils import time_usage

class Dataset:

	def __init__(self, filepath):
		self.filepath = filepath
		self.load()
		self.preprocess()

	@time_usage("Loading dataset...")
	def load(self):

		dataset = open(self.filepath)
		self.lines = dataset.readlines()
		

	def preprocess(self):
		self.lines = self.fix_non_unicode()
		self.lines = self.remove_duplicates()		

	@time_usage("Fixing non-unicode characters...")
	def fix_non_unicode(self):
		return [line.decode('unicode_escape').encode('ascii', 'ignore') for line in self.lines]

	@time_usage("Removing duplicates...")
	def remove_duplicates(self):
		newlist = []
		for line in self.lines:
			if line not in newlist:
				newlist.append(line)
		return newlist

