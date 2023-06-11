#!/usr/bin/env python3

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    # TODO: Language detection :)
    filtered_tokens = [
        token for token in tokens if token not in stopwords.words("english")
    ]

    # Will convert different variations of words all into the same one
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    preprocess_text = " ".join(lemmatized_tokens)
    return preprocess_text


analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores["compound"]


while True:
    review = input("Your text: ")
    processed = preprocess_text(review)
    print("Processed: " + processed)
    print(get_sentiment(processed))
