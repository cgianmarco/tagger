import matplotlib.pyplot as plt
import numpy as np

class MatrixVisualizer:

	def __init__(self, tagger):
		self.tagger = tagger


	def run(self, filename):

		cooccurrence = np.array(self.tagger.cooccurrence.todense())
		tags = self.tagger.tags
		# Plot it out
		fig, ax = plt.subplots()
		heatmap = ax.pcolor(cooccurrence, cmap=plt.cm.Blues, alpha=0.9)

		fig = plt.gcf()
		fig.set_size_inches(8,8)

		# turn off the frame
		ax.set_frame_on(False)

		# put the major ticks at the middle of each cell
		ax.set_yticks(np.arange(cooccurrence.shape[0])+0.5, minor=False)
		ax.set_xticks(np.arange(cooccurrence.shape[1])+0.5, minor=False)

		# want a more natural, table-like display
		ax.invert_yaxis()
		ax.xaxis.tick_top()

		# Set the labels
		labels = tags

		# note I could have used nba_sort.columns but made "labels" instead
		ax.set_xticklabels(labels, minor=False) 
		ax.set_yticklabels(labels, minor=False)

		# rotate the 
		plt.xticks(rotation=90)

		ax.grid(False)

		# Turn off all the ticks
		ax = plt.gca()

		for t in ax.xaxis.get_major_ticks(): 
		    t.tick1On = False 
		    t.tick2On = False 
		for t in ax.yaxis.get_major_ticks(): 
		    t.tick1On = False 
		    t.tick2On = False
		plt.savefig("generated/visualization/" + filename + ".png", bbox_inches='tight')
		plt.close()





class WordVectorVisualizer:

	def __init__(self, tagger):
		self.tagger = tagger

	def run(self, n_tags, filename):
		tags = self.tagger.tags[:n_tags]
		cooccurrence = np.array(self.tagger.cooccurrence.todense())

		la = np.linalg

		U, s, Vh = la.svd(cooccurrence, full_matrices=False)

		for i in xrange(len(tags)):
			plt.text(U[i, 0], U[i, 1], tags[i])

		plt.axis([-1.2, 1.2, -1.2, 1.2])


		plt.savefig("generated/visualization/" + filename + ".png")
		plt.close()