# tagger

[Generated single word tags](generated/tags_single.txt)

[Generated double word tags](generated/tags_double.txt)

[Generated triple word tags](generated/tags_triple.txt)


# Testing

```
python test/taggers_unittest.py -v
```


# Usage

```
python run.py
```


# Customize

In run.py create new configuration dictionary

```
my_conf = { 	
					'max_df': 0.95, 
					'min_df': 2,
					'token_pattern': '(?u)\\b\\w\\w+\\b',
					'ngram_range': (2,2)
				}
```


Then create new Tagger, run it on dataset and print number of tagged elements

```
myTagger = Tagger(my_conf)
myTagger.run(500, dataset.lines, "myconf")

print "Tagged elements with single tags: " + str(myTagger.get_tagged_elements())
```

Generated tags can be found in generated/tags_myconf.txt

```
pokemon
mint
serie
misura
plastica
```