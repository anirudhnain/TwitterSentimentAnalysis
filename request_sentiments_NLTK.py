import requests
import json
file_data = open("clean_extracted_text")
url = r"http://text-processing.com/api/sentiment/" 
for line in file_data:
	payload = { 'text' : line }
	res = requests.post(url, data=payload)
	for data in res:
		print data+'\n'
		# d = json.loads(data)
		# print "\tPolarity: ",d["label"]
		# print "\t\tPositive: ",d["probability"]["pos"],
		# print "\tNegative: ",d["probability"]["neg"],
		# print "\tNeutral: ",d["probability"]["neutral"]