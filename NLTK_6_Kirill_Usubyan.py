import nltk
import random
from nltk.corpus import movie_reviews

print("CHAPTER 6 EXERCISE 4")
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2500]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print("30 most important classifier features: ")
print(classifier.show_most_informative_features(30))
print("Some of these classifier features are understandable, and make logical sense in a movie review. ")
print("However many of them seem purely correlational, showing the weakeness of th this classifier, at least on this data set.")
print("For instance 'miscast', 'ugh', 'sexist', 'poorly' and 'ridiculous' are clearly strong indicators of a negative review.")
print("But many are not based on data so much as a strange correlation, like 'schumacher' and 'justin' with negative reviews.")