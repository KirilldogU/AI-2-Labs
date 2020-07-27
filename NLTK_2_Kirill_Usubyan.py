import nltk
import random
#nltk.download()
from nltk.corpus import state_union, wordnet, udhr
print()
print("EXTRA EXERCISE:")
print("CHAPTER 2 Exercise 25: ")
def find_language(wordTested):
    latinLanguages = list()
    for language in udhr.fileids():
        if 'Latin1' in language:
            latinLanguages.append(language)
    languageContains = list()
    for latinlanguage in latinLanguages:
        if wordTested in udhr.words(latinlanguage):
            languageContains.append(latinlanguage)
    return languageContains
print("According to corpus.udhr the word 'war' is used in languages:")
print(find_language("war"))
print()
#EXERCISE 4
numMen =0
numWomen = 0
numPeople = 0
for word in state_union.words():
    #print(word)
    if word == "PEOPLE".lower():
        numPeople+=1
    if word == "MEN".lower():
        numMen+=1
    if word == "WOMEN".lower():
        numWomen+=1
print("CHAPTER 2 EXERCISE 4")
print("NUM PEOPLE " + str(numPeople) + " NUM MEN " + str(numMen) + " NUM WOMEN " + str(numWomen))
print()

#EXERCISE 5
#Holonyms are words that are the larger group under which a word falls
#Meronyms are the smaller words included
from nltk.corpus import wordnet #semantic dictionary
print("CHAPTER 2 EXERCISE 5")
randomWordSynset = "world.n.01"
print("RANDOM WORD: " + randomWordSynset)
print("PART MERONYMS: " + str(wordnet.synset(randomWordSynset).part_meronyms()))
print("MEMBER MERONYMS: " + str(wordnet.synset(randomWordSynset).member_meronyms()))
print("SUBSTANCE MERONYMS: " + str(wordnet.synset(randomWordSynset).substance_meronyms()))
print("MEMBER HOLONYMS: " + str(wordnet.synset(randomWordSynset).member_holonyms()))
print("PART HOLONYMS: " + str(wordnet.synset(randomWordSynset).part_holonyms()))
print("SUBSTANCE HOLONYMS: " + str(wordnet.synset(randomWordSynset).substance_holonyms()))
print()
randomWordSynset = "root.n.01"
print("RANDOM WORD: " + randomWordSynset)
print("PART MERONYMS: " + str(wordnet.synset(randomWordSynset).part_meronyms()))
print("MEMBER MERONYMS: " + str(wordnet.synset(randomWordSynset).member_meronyms()))
print("SUBSTANCE MERONYMS: " + str(wordnet.synset(randomWordSynset).substance_meronyms()))
print("MEMBER HOLONYMS: " + str(wordnet.synset(randomWordSynset).member_holonyms()))
print("PART HOLONYMS: " + str(wordnet.synset(randomWordSynset).part_holonyms()))
print("SUBSTANCE HOLONYMS: " + str(wordnet.synset(randomWordSynset).substance_holonyms()))
print()
randomWordSynset = "party.n.01"
print("RANDOM WORD: " + randomWordSynset)
print("PART MERONYMS: " + str(wordnet.synset(randomWordSynset).part_meronyms()))
print("MEMBER MERONYMS: " + str(wordnet.synset(randomWordSynset).member_meronyms()))
print("SUBSTANCE MERONYMS: " + str(wordnet.synset(randomWordSynset).substance_meronyms()))
print("MEMBER HOLONYMS: " + str(wordnet.synset(randomWordSynset).member_holonyms()))
print("PART HOLONYMS: " + str(wordnet.synset(randomWordSynset).part_holonyms()))
print("SUBSTANCE HOLONYMS: " + str(wordnet.synset(randomWordSynset).substance_holonyms()))
print()
#EXERCISE 7
print("CHAPTER 2 EXERCISE 7")
#Concordance displays the use of a word in the context of a text sample
corpusUsed = nltk.corpus.state_union
print("Concordance of 'However' in the State of the Union Addresses:")
concordance = nltk.Text(state_union.words()).concordance("however")
print(concordance)
print()
#EXERCISE 9
from nltk.book import *
print("CHAPTER 2 EXERCISE 9")
firstText = text7 #THE WALL STREET JOURNAL
secondText = text3 #THE BOOK of Genesis
print("FIRST TEXT " + str(firstText))
print("SECOND TEXT " + str(secondText))
wordCompared = "raise"
print("Words similar to '" + wordCompared + "' in " + str(firstText))
print(firstText.similar(wordCompared))
print("Words similar to '" + wordCompared + "' in " + str(secondText))
print(secondText.similar(wordCompared))
#EXERCISE 12
print("CHAPTER 2 EXERCISE 12")  #CHECK
wordPronounciationEntries = nltk.corpus.cmudict.entries()
pronounciationdict = nltk.corpus.cmudict.dict()
numWords = len(pronounciationdict.keys())
numSeveralPronounciations = 0
for word, pronounciation in wordPronounciationEntries:
    pronounciationNumber = len(pronounciationdict[word])
    if pronounciationNumber > 1:
        numSeveralPronounciations+=1
print("NUMBER OF WORDS IN CMU DICTIONARY: " + str(numWords))
print("NUMBER OF WORDS WITH SEVERAL PRONOUNCIATIONS: " + str(numSeveralPronounciations))
print()
#EXERCISE 17
print("CHAPTER 2 EXERCISE 17")
from nltk.corpus import stopwords
stopwordsEnglish = stopwords.words('english')
wordsWallStreet = [word.lower() for word in text7 if word.lower() not in stopwordsEnglish]
newWordWallStreet = list()
for wordW in wordsWallStreet:
    if wordW.isalpha():
        newWordWallStreet.append(wordW)
freqDist = FreqDist(newWordWallStreet)
print("50 most Frequent non-stopwords in  Wall Street Journal:")
print(freqDist.most_common(50))
print()
#EXERCISE 18
print("CHAPTER 2 EXERCISE 18")
genesisBigrams = nltk.bigrams(text3)
newGenesisBigrams = list()
for bigram in genesisBigrams:
    inBigram = False
    for partOfBigram in bigram:
        if partOfBigram.lower() in stopwordsEnglish:
            inBigram = True
        if partOfBigram.isalpha() == False: #tests for punctuation
            inBigram = True
    if inBigram == False:
        newGenesisBigrams.append(bigram)
genesisFreqDist = nltk.FreqDist(newGenesisBigrams)
print("50 most common non-stopword bigrams in Book of Genesis")
print(genesisFreqDist.most_common(50))
print()
#EXERCISE 23
print("CHAPTER 2 EXERCISE 23")
import matplotlib.pyplot
def zipf_plot(text):
    freqDistZipf = FreqDist(text)
    numWords = len(freqDistZipf.keys())
    place = 1
    x = []  #place in order
    y = []  #frequency
    for wordCommon in freqDistZipf.most_common(numWords):
        wordCom, other = wordCommon
        frequency = freqDistZipf[wordCom]
        x.append(place)
        y.append(frequency)
        place+=1
    area = 15
    matplotlib.pyplot.scatter(x, y, s=area, alpha=0.5)
    matplotlib.pyplot.title('Zipf plot')
    matplotlib.pyplot.xlabel('Place in Commonness of Word')
    matplotlib.pyplot.ylabel('Frequency of Word')
    matplotlib.pyplot.show()
zipf_plot(newWordWallStreet)        #part a
print("ZIPF PLOT confirms inverse relation between rank of word and frequency.")

from nltk.tokenize import word_tokenize

randomStr = ""
for x in range(100000):
    randomStr += random.choice("abcdefg ")
zipf_plot(randomStr.split())
print("The Zipf plot also holds for a randomly generated string.")
print()
#EXERCISE 27

print("CHAPTER 2 EXERCISE 27")
numSenses = 0
numWords = 0
totalLemmas1 = set()
for synset in list(wordnet.all_synsets(wordnet.NOUN)):
    lemmas = synset.lemmas()
    for lemma in lemmas:
        name = lemma.name()
        if name not in totalLemmas1:
            totalLemmas1.add(name)
            numWords += 1
            numSenses += len(wordnet.synsets(lemma.name(), wordnet.NOUN))

print("The average wordnet noun has a polysemy of  " + str(numSenses/numWords))

numSenses = 0
numWords = 0
totalLemmas2 = set()
for synset in list(wordnet.all_synsets(wordnet.ADJ)):
    lemmas = synset.lemmas()
    for lemma in lemmas:
        name = lemma.name()
        if name not in totalLemmas2:
            totalLemmas2.add(name)
            numWords += 1
            numSenses += len(wordnet.synsets(lemma.name(), wordnet.ADJ))

print("The average wordnet adjective has a polysemy of  " + str(numSenses/numWords))

numSenses = 0
numWords = 0
totalLemmas3 = set()
for synset in list(wordnet.all_synsets(wordnet.ADV)):
    lemmas = synset.lemmas()
    for lemma in lemmas:
        name = lemma.name()
        if name not in totalLemmas3:
            totalLemmas3.add(name)
            numWords += 1
            numSenses += len(wordnet.synsets(lemma.name(), wordnet.ADV))

print("The average wordnet adverb has a polysemy of  " + str(numSenses/numWords))

numSenses = 0
numWords = 0
totalLemmas4 = set()
for synset in list(wordnet.all_synsets(wordnet.VERB)):
    lemmas = synset.lemmas()
    for lemma in lemmas:
        name = lemma.name()
        if name not in totalLemmas4:
            totalLemmas4.add(name)
            numWords += 1
            numSenses += len(wordnet.synsets(lemma.name(), wordnet.VERB))

print("The average wordnet verb has a polysemy of  " + str(numSenses/numWords))