import nltk,pickle
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
import os
import subprocess
import neg

text = open("final_movie_tweet")
thefile = open("thefile", "w")
st = LancasterStemmer()
stop = stopwords.words('english')
tweet_arr = []
#loadng sentic words
with open("sentic_score", 'rb') as f:
	my_list = pickle.load(f)
for line in text:
	# print line,
	# stop words removal
	line = line.lower()
	line = " ".join([i for i in line.split() if i not in stop])

	# stemming
	tokens = line.split()
	for i in range(len(tokens)):
		tokens[i] = st.stem(tokens[i])

	line = " ".join(tokens)
	tweet_arr.append(line)
	print >> thefile, line


#pos tagging
proc = subprocess.Popen(["./runTagger.sh --output-format conll thefile"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
tokens = []; sub_token = []
for line in out.split("\n"):
	# print line
	if line:
		sub_token.append(line.split())
	if line == '':
		# print sub_token
		tokens.append(sub_token)
		sub_token = []

# negation handling
n = neg.neg()
token_count = 0
print 
for token in tokens:
	sco = n.get_sentiments(token)
	if sco>0:
		print "Positive Tweet:",tweet_arr[token_count]
	elif sco<0:
		print "Negative Tweet:",tweet_arr[token_count]
	else:
		print "Neutral_Tweet:",tweet_arr[token_count]
	token_count+=1

"""

	#removing tweet specific words
	words = ['rt',':','@','http','the']
	pos_score = 0
	neg_score = 0
	count = 0
	for elem in tokens:
		elem_count = 0
		elem_pos= elem_neg =0
		if elem not in words:
			for sentic_score in my_list:
				sentic_word = sentic_score[2]
				if elem in sentic_word:
					elem_pos+=float(sentic_score[0])
					elem_neg+=float(sentic_score[1])
					elem_count+=1
		if elem_count:
			pos_score+=elem_pos/elem_count
			neg_score+=elem_neg/elem_count
			count+=1

	if count!=0:
		pos_sentiment = pos_score/count
		neg_sentiment = neg_score/count
		if neg_sentiment and pos_sentiment/neg_sentiment>1.5:
			print "Pos_Tweet"
		elif pos_sentiment and neg_sentiment/pos_sentiment>1.5:
			print "Neg_Tweet"
		else:
			print "Neutral_Tweet"
	else:
		print "Neutral_Tweet"
	print 
"""