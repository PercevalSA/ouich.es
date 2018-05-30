#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import json, requests, wget
from bs4 import BeautifulSoup

url = "http://ouich.es"
citations = []

# getting quotes list
response = requests.get(url)
response.encoding = 'utf-8'

if response.status_code == 200:
	soup = BeautifulSoup(response.text, 'html.parser')
	tags = soup.find_all("a", {"class": "tag"})
	
	# for each quote get description and mp3 file
	for tag in tags:

		uri = tag['href']
		response = requests.get(url + uri)
		response.encoding = 'utf-8'

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, 'html.parser')
			citation = soup.find("div", { "class" : "citation" })
			description = citation.contents
			filename = uri[5:]

			to_add = {
				'character': filename,
				'file': filename + '.mp3',
				'title': description[0]
			}

			citations.append(to_add)
			file = wget.download(url + '/mp3/' + filename + '.mp3')

# writing result to file
data = json.dumps(citations, indent=4, ensure_ascii=False)
with open('sounds.json', 'w', encoding="utf-8") as f: 
	f.write(data)
