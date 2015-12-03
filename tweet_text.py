input_file = open("movie_data.20150922-175151.json")

for lines in input_file:
	if lines:
		if "text" in lines:
			print lines.split("text")[1].split(',')[0][2:]