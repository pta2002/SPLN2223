from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [
        token for token in tokens if token not in stopwords.words("english")
    ]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    preprocessed_text = " ".join(lemmatized_tokens)
    return preprocessed_text


analyzer = SentimentIntensityAnalyzer()


def get_polarity_scores(text):
    return analyzer.polarity_scores(preprocess_text(text))
