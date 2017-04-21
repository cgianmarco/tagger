from core.dataset import *
from core.taggers import Tagger
from core.visualizers import MatrixVisualizer, WordVectorVisualizer
from nltk.corpus import stopwords

dataset = Dataset("dataset/prodotti.csv")


single_tagger = { 	
					'max_df': 0.95, 
					'min_df': 2,
					'max_features': 500, 
					'token_pattern': '(?u)\\b\\w\\w\\w+\\b',
					'stop_words': stopwords.words('italian')
				}

double_tagger = { 	
					'max_df': 0.95, 
					'min_df': 2,
					'max_features': 500, 
					'token_pattern': '(?u)\\b\\w\\w+\\b',
					'ngram_range': (1,4),
					'stop_words': stopwords.words('italian')
				}

triple_tagger = { 	
					'max_df': 0.95, 
					'min_df': 2,
					'max_features': 500, 
					'token_pattern': '(?u)\\b\\w\\w+\\b',
					'ngram_range': (3,3)
				}


swt = Tagger(dataset, single_tagger)
swt.run("single")

dwt = Tagger(dataset, double_tagger)
dwt.run("double")

twt = Tagger(dataset, triple_tagger)
twt.run("triple")

print "Tagged elements with single tags: " + str(swt.get_tagged_elements())
print "Tagged elements with double tags: " + str(dwt.get_tagged_elements())
print "Tagged elements with triple tags: " + str(twt.get_tagged_elements())


# Matrix visualization

# mv = MatrixVisualizer(swt)
# mv.run("single_matrix");

# mv = MatrixVisualizer(dwt)
# mv.run("double_matrix");

# mv = MatrixVisualizer(twt)
# mv.run("triple_matrix");


# Word Vectors

# wvv = WordVectorVisualizer(swt)
# wvv.run(5, "single_vectors")

# wvv = WordVectorVisualizer(dwt)
# wvv.run(5, "double_vectors")

# wvv = WordVectorVisualizer(twt)
# wvv.run(5, "triple_vectors")

