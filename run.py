from core.dataset import *
from core.taggers import SingleWordTagger, DoubleWordTagger

n_single_tags = 20
n_double_tags = 100

dataset = Dataset()
words = dataset.get_words()

# tg = SingleWordTagger()
# tg.run(words, n_single_tags)

tg = DoubleWordTagger()
tg.run(words, n_double_tags)
