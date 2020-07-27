import nltk, re, pprint
from nltk.corpus import *
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

print("CHAPTER 3 EXERCISE 20")
url = "https://ion.tjhsst.edu"
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = re.split(r'[ \t\n]+', raw)
print("Accessing site: " + url)
print("First 15 tokens of site (including header):")
print(tokens[:15])
print()


print("CHAPTER 3 EXERCISE 22")
url2 = "http://news.bbc.co.uk/"
html = request.urlopen(url2).read().decode('utf8')
rawText = BeautifulSoup(html, 'html.parser').get_text()
splitText = re.split(r'[ \t\n]+', rawText)
wordText = [word for word in splitText if re.search('^(?![_;=()])\w+\w$', word)]
finishedText = ' '.join(wordText)
print("Accessing site: " + url2)
print(finishedText)