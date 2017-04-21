import unittest

import sys, os
sys.path.append(os.path.abspath(sys.path[0]) + '/../')

from core.taggers import Tagger


class TestTagger(unittest.TestCase):
 
    def setUp(self):

    	self.testconfig = { 
					'token_pattern': '(?u)\\b\\w+\\b'
				}

        self.tagger = Tagger(self.testconfig)
        self.testline = ["This is a very very good sentence"]
 
    def test_run(self):
        self.assertEqual(True, self.tagger.run(6, self.testline, "test"))
 
    def test_tags(self):
    	self.tagger.run(6, self.testline, "test")
    	self.assertEqual(6, len(self.tagger.tags))

    def test_tag2frequency(self):
    	self.tagger.run(6, self.testline, "test")
    	self.assertEqual("very", self.tagger.tag2frequency.keys()[0])

    def test_tagged_elements(self):
    	self.tagger.run(6, self.testline, "test")
    	self.assertEqual(1, self.tagger.get_tagged_elements())


if __name__ == '__main__':
    unittest.main()

