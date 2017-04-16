from core.dataset import *
from core.taggers import SingleWordTagger, DoubleWordTagger

n_single_tags = 300
n_double_tags = 300

dataset = Dataset()

swt = SingleWordTagger(dataset)
swt.run(n_single_tags, mf=False)

dwt = DoubleWordTagger(dataset)
dwt.run(n_double_tags)
