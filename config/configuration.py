import nltk

mongo_uri = 'mongodb://localhost:27017/lotr'
nltk.downloader.download('vader_lexicon')
nltk.download('stopwords')  # stopwords