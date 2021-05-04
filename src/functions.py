
from bson.objectid import ObjectId

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords


def create_document(mongo, char, dialog, movie):
    """Inserts a new entry in the database
    Receives: mongo, char, dialog, movie
    Return: new document
    """
    _id = mongo.db.lotr_characters.insert(
        {'char': char, 'dialog': dialog, 'movie': movie}
    )
    response = {
        '_id': str(_id),
        'char': char,
        'dialog': dialog,
        'movie': movie
    }
    return response


def get_document_by_id(mongo, _id=None):
    """Get information from the db
    Receives: mongo, _id (if specified)
    Return: the query in the database with the indicated filters
    """
    if _id is None:
        return mongo.db.lotr_characters.find()
    else:
        return mongo.db.lotr_characters.find_one({'_id': ObjectId(_id)})


def get_documents(mongo, key, value=None):
    """Get specific information from the db
    Receives: mongo, key(in DB fail movie or char), value(movie or character we are looking for)
    Return: the query in the database with the indicated filters
    """
    if key is None or value is None:
        return mongo.db.lotr_characters.find()
    else:
        return mongo.db.lotr_characters.find({key: value})


def delete_document(mongo, _id):
    """Delete document from id
    Receives: mongo, _id
    """
    return mongo.db.lotr_characters.delete_one({'_id': ObjectId(_id)})


def update_document(mongo, _id, char, dialog, movie):
    """Update an existing entry in the database
    Receives: mongo, _id, char, dialog, movie
    """
    response = mongo.db.lotr_characters.update_one({'_id': ObjectId(_id)}, {'$set': {
        'char': char,
        'dialog': dialog,
        'movie': movie
        }})

    return response


def get_analysis(mongo, _id):
    """ application of one of the NLTK libraries,
    to process dialogues and obtain sentiment analysis.
    Receives: mongo, _id
    Return: dialogue text and its polarity
    """
    dialog = mongo.db.lotr_characters.find_one({'_id': ObjectId(_id)})
    text = dialog['dialog']

    # do sentiment analysis from 'text'
    # stop_words = set(stopwords.words('english'))

    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(text)
    pol = polarity['compound']
    response = {
        'dialog': text,
        'polarity': polarity
    }

    return response



