import pickle

lines = open("SentiWordNet.txt")
lists = []
for line in lines:
	words = line.split()
	l = []
	if len(words)>=5:
		l.append(words[2])	#pos_score
		l.append(words[3])	#neg_score
		for i in range(4,len(words)):
			new_l = l[:]
			if '#' in words[i]:
				new_l.append(words[i])	#word
				lists.append(new_l)
with open("sentic_score", 'wb') as f:
    pickle.dump(lists, f)
with open("sentic_score", 'rb') as f:
    my_list = pickle.load(f)
    count = 0
    for lm in my_list:
    	print lm
    	if count==10:
    		break
    	count+=1