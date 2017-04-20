from core.dataset import *
from core.taggers import SingleWordTagger, DoubleWordTagger
from core.visualizers import MatrixVisualizer, WordVectorVisualizer

n_single_tags = 20
n_double_tags = 20

dataset = Dataset()

swt = SingleWordTagger(dataset)
swt.run(n_single_tags, save=False, mf=False)

dwt = DoubleWordTagger(dataset)
dwt.run(n_double_tags, save=False, mf=False)

print "Tagged elements with single tags: " + str(swt.get_tagged_elements())
print "Tagged elements with double tags: " + str(dwt.get_tagged_elements())

mv = MatrixVisualizer(swt)
mv.run("single_matrix");

mv = MatrixVisualizer(dwt)
mv.run("double_matrix");

wvv = WordVectorVisualizer(swt)
wvv.run(5, "single_vectors")

wvv = WordVectorVisualizer(dwt)
wvv.run(5, "double_vectors")

