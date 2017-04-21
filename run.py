from core.dataset import *
from core.taggers import Tagger
from core.visualizers import MatrixVisualizer, WordVectorVisualizer
from nltk.corpus import stopwords

dataset = Dataset("dataset/prodotti.csv")


single_tagger = { 	
					'max_df': 0.95, 
					'min_df': 2,
					'token_pattern': '(?u)\\b\\w\\w\\w+\\b',
					'stop_words': stopwords.words('italian')
				}

double_tagger = { 	
					'max_df': 0.95, 
					'min_df': 2,
					'token_pattern': '(?u)\\b\\w\\w+\\b',
					'ngram_range': (2,2)
				}

triple_tagger = { 	
					'max_df': 0.95, 
					'min_df': 2,
					'token_pattern': '(?u)\\b\\w\\w+\\b',
					'ngram_range': (3,3)
				}


swt = Tagger(single_tagger)
swt.run(500, dataset.lines, "single")

dwt = Tagger(double_tagger)
dwt.run(500, dataset.lines, "double")

twt = Tagger(triple_tagger)
twt.run(500, dataset.lines, "triple")

print "Tagged elements with single tags: " + str(swt.get_tagged_elements())
print "Tagged elements with double tags: " + str(dwt.get_tagged_elements())
print "Tagged elements with triple tags: " + str(twt.get_tagged_elements())




