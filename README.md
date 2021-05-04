

# Project: Api-Sentiment
## by Susana Martin Wanton

## Goal: Programming an API that:

Serve and receive information for customers (in response to CRUD requests).

The data used to create the database is based on the Lord of the Rings movie series.

The Lord of the Rings is an epic high fantasy novel by the English author and scholar J. R. R. Tolkien. Set in Middle-earth, the world at some distant time in the past, the story began as a sequel to Tolkien's 1937 children's book The Hobbit, but eventually developed into a much larger work. Written in stages between 1937 and 1949, The Lord of the Rings is one of the best-selling books ever written, with over 150 million copies sold.

---

## Procedure:

### Start up

```bash
1-(main_lotr.py)
```

Database system: MongoDB
Framework:Flask
Test platform for API development: Postman


### API

- main_lotr.py:main API file - provides the Endpoints.

    - config.configuration.py: connect to Mongo database.

    - src.functions.py: file with the code of functions used for the Endpoints.

####Endpoints:
(POST)   /Create route that allows including data
(GET)    /Create a route that allows you to list all documents
(GET)    /Create a route that allows listing a single document (the first of all)
(GET)    /Create a route that allows you to list all movie
(GET)    /Create a route that allows you to list all characters
(GET)    /Create a path that allows the sentiment analysis of a dialogue
(DELETE) /Create a route that allows you to delete document
(PUT)    /Create a route to update documents


### Sentiment analysis

```bash
2-(sentiment_analysis_lotr.ipynb)
```

#### 1. Load .csv

#### 2. Tokenization
- Process of dividing a string of written language into its component words.

#### 3. Stop words
- Stop Words with NLTK — eliminating the words that are in the stop words list.

#### 4. Sentiment analysis
- Using NLTK to classify the polarity of a given text. — returns whether the expressed opinion in the dialog is positive, negative, or neutral. 

#### 5. Graphical visualizations
- Distribution of characters according to the polarity analysis of the dialogues

```bash
2(sentiment_analysis_01.png)
3(sentiment_analysis_02.png)
```

---
## Dependencies used

click==7.1.2
Flask==1.1.2
Flask-PyMongo==2.3.0
itsdangerous==1.1.0
Jinja2==2.11.3
joblib==1.0.1
MarkupSafe==1.1.1
nltk==3.6.2
pymongo==3.11.3
regex==2021.4.4
tqdm==4.60.0
Werkzeug==1.0.1

---
## Resources used

* [Python Functional Programming How To Documentation](https://docs.python.org/3.7/howto/functional.html]
* [Python Errors and Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html]
* [StackOverflow String Operation Questions](https://stackoverflow.com/questions/tagged/string+python]
* [https://docs.mongodb.com/manual/geospatial-queries/]
* [https://www.getpostman.com/]
* [https://www.nltk.org/]
* [https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]
* [https://en.wikipedia.org/wiki/Sentiment_analysis]

