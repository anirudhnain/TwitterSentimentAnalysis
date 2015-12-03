import pickle
class neg():
	def __init__(self):
		
		with open("sentic_score", 'rb') as f:
			self.my_list = pickle.load(f)

	def get_token_score(self,token):
		token_pos=token_neg=token_count=pos_score= neg_score=0
		for sentic_score in self.my_list:
			#print sentic_score
			sentic_word = sentic_score[2]
			if token == sentic_word[:-2]:
				# token_pos = max(token_pos,float(sentic_score[0]))
				token_pos += float(sentic_score[0])
				token_neg += float(sentic_score[1])
				token_count += 1
				if token_pos==0 and token_neg==0:
					token_count-=1
		# print token_pos,token_neg,token_count
		if token_count:
			pos_score = token_pos/token_count
			neg_score = token_neg/token_count
		# print pos_score,neg_score
		# print token_pos
		if pos_score>neg_score:
			return pos_score	
		else:
			return -1*neg_score
			

	def get_sentiments(self, tokens):
		list_negation_words = ['nor','useless','no','never','not','without','against',"n't","nt"]
		#check for n't and nt
		# line = "We don't care about nwea."
		sentence_end = [".",",",";",":",".","and","&","or","but",'?']
		#Do this after tokenization
		score = 0
		#loadng sentic words
		token_count = 0
		for token in tokens:
			# print "Score:"
			token_score = self.get_token_score(token[0])
			#print "Token_Score:",token_score
			score_neg = -1
			neg_word = False
			neg_score = 0
			if token[0] in list_negation_words:
				neg_word = True
				neg_score = 0
			elif token[0] in sentence_end:
				if token[0] != '?' and neg_word:	#Consider negation if tweet is not a question
					score = -1*(neg_score)
				neg_word = False
			elif neg_word:
				neg_score += (token_score)
			else:
				# print "token_score:",token_score
				score += (token_score)
			if token_score!=0.0:
				token_count+=1
		if score>0.1 or score<(-0.1):
			return score/token_count
		else:
			return 0.0

# s = [["This",'a'],["movie",'a'],["suck",'a']]
# n = neg()
# print n.get_sentiments(s)