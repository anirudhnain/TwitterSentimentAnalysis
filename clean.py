clean_text = open("movie_tweets")
for line in clean_text:
	newline = ""
	i = 0 
	while i < len(line):
		if line[i] == '\\':
			while i < len(line) and (line[i]!= '\t' or line[i]!= '\n' or line[i]!= ''):
				i+=1
		if i < len(line):
			newline += line[i]
			i+=1
	newline = newline.strip()
	if newline and newline[-1] != '"':
		print newline