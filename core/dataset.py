import utils

class Dataset:

	def __init__(self):
		self.data = open('dataset/prodotti.csv')
		self.data = self.data.read()
		self.preprocess()

	def preprocess(self):
		# Leave only alphabetic characters or spaces
		self.data = utils.letters(self.data)

		# Split into words
		self.words = self.data.split()

		# Fix non-unicode chars
		self.words = [word.decode('unicode_escape').encode('ascii', 'ignore') for word in self.words]

		# All lowercase
		self.words = [word.lower() for word in self.words]

		# Remove italian common words
		self.words = utils.no_stopwords(self.words)

		# Remove short words
		self.words = [word for word in self.words if len(word) > 2] 

	def get_words(self):
		return self.words
