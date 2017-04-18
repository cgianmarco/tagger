from core.dataset import *
from core.taggers import SingleWordTagger, DoubleWordTagger
from core.visualizers import MatrixVisualizer, WordVectorVisualizer

n_single_tags = 5
n_double_tags = 500

dataset = Dataset()

swt = SingleWordTagger(dataset)
swt.run(n_single_tags)

# dwt = DoubleWordTagger(dataset)
# dwt.run(n_double_tags)

# mv = MatrixVisualizer(swt)
# mv.run();

# wvv = WordVectorVisualizer(swt)
# wvv.run(5)

