import utils

class Dataset:

	def __init__(self):
		dataset = open('dataset/prodotti.csv')
		self.data = dataset.read()

		dataset = open('dataset/prodotti.csv')
		self.lines = dataset.readlines()
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


		

		self.lines = [utils.letters(line) for line in self.lines]

		self.lines = [line.strip() for line in self.lines]

		# Fix non-unicode chars
		self.lines = [line.decode('unicode_escape').encode('ascii', 'ignore') for line in self.lines]

		# All lowercase
		self.lines = [line.lower() for line in self.lines]

	def get_words(self):
		return self.words

	def get_lines(self):
		return self.lines