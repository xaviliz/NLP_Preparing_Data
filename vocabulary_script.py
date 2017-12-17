# Develope a Vocabulary

import string
import re
from os import listdir
from collections import Counter
from nltk.corpus import stopwords

# load doc into memory
def load_doc(filename):
	# open the file as read only 
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file file.close()
	return text

# turn a doc into clean tokens
def clean_doc(doc):
	# split into tokens by white space
	tokens = doc.split()
	# prepare regex for char filtering
	re_punc = re.compile('[%s]' % re.escape(string.punctuation)) 
	# remove punctuation from each word
	tokens = [re_punc.sub('', w) for w in tokens]
	# remove remaining tokens that are not alphabetic
	tokens = [word for word in tokens if word.isalpha()]
	# filter out stop words
	stop_words = set(stopwords.words('english'))
	tokens = [w for w in tokens if not w in stop_words]
	# filter out short tokens
	tokens = [word for word in tokens if len(word) > 1]
	return tokens

# load doc and add to vocab
def add_doc_to_vocab(filename, vocab):
  # load doc
  doc = load_doc(filename)
  # clean doc
  tokens = clean_doc(doc)
  # update counts
  vocab.update(tokens)

# load all docs in a directory
def process_docs(directory, vocab):
	# walk through all files in the folder
	for filename in listdir(directory):
		#print filename
		# skip files that do not have the right extension
		if not filename.endswith(".txt"):
			next
		# create the full path of the file to open
		path = directory + '/' + filename 
		# add doc to vocab 
		add_doc_to_vocab(path, vocab)
		#print path

# save list to file
def save_list(lines, filename): 
	data = '\n'.join(lines)
	file = open(filename, 'w') 
	file.write(data)
	file.close()

# define vocab
vocab = Counter()
# add all docs to vocab
process_docs('txt_sentoken/neg', vocab) 
process_docs('txt_sentoken/pos', vocab) 
# print the size of the vocab 
print("number of words in the vocabulary: " + str(len(vocab)))
# print the top words in the vocab
print(vocab.most_common(50))

# FILTERING BY OCCURRENCE
# keep tokens with > 5 occurrence
min_occurane = 5
tokens = [k for k,c in vocab.items() if c >= min_occurane] 
print(len(tokens))
# save tokens to a vocabulary file
save_list(tokens, 'vocab.txt')

