import json
import re
import operator
import json
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string

nltk.data.path.append('path_to_nltk_data')

emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


# Getting common, insignificant words for NLTK
punctuation = list(string.punctuation)
common_words = stopwords.words('english') + punctuation + ['rt', 'via']


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

class tweetParser():

    global tokens_re
    global emoticon_re
    global common_words

    @classmethod
    def read_and_tokenize_file(self, file_name):
        with open(file_name, 'r') as f:
            for line in f:
                tweet = json.loads(line)
                tokens = preprocess(tweet['text'])
                #print(tokens)
                return tokens

    @classmethod
    def count_word_frequencies(self, file_name):
        with open(file_name, 'r') as f:
            count_all = Counter()
            for line in f:
                tweet = json.loads(line)
                # Create a list with all the terms
                terms = [term for term in preprocess(tweet['text']) if term not in common_words]
                # Update the counter
                count_all.update(set(terms))
            # Print the first 20 most frequent words
            print "--------------MOST COMMON WORDS:-------"
            print(count_all.most_common(20))
            return count_all.most_common(20)



