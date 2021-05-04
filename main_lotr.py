from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import src.functions as ft
from config.configuration import mongo_uri

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)
app.config['MONGO_URI'] = mongo_uri
mongo = PyMongo(app)


# Create route that allows including data
@app.route('/lotr_characters', methods=['POST'])
def create_document():
    # Receiving data
    char = request.json['char']
    dialog = request.json['dialog']
    movie = request.json['movie']

    if char and dialog and movie:
        response = ft.create_document(mongo, char, dialog, movie)
    else:
        return not_found()

    return response


# Create a route that allows you to list all documents
@app.route('/lotr_characters', methods=['GET'])
def get_documents():
    document = ft.get_document_by_id(mongo=mongo)
    response = json_util.dumps(document)
    return Response(response, mimetype='application/json')


# Create a route that allows listing a single document (the first of all)
@app.route('/lotr_characters/<_id>', methods=['GET'])
def get_document(_id):
    document = ft.get_document_by_id(mongo=mongo, _id=_id)
    if not document:
        return not_found()

    response = json_util.dumps(document)
    return Response(response, mimetype='application/json')


# Create a route that allows you to list all movie
@app.route('/lotr_characters/movie/<movie>', methods=['GET'])
def get_movie(movie):
    document = ft.get_documents(mongo=mongo, key='movie', value=movie)
    if not document:
        return not_found()

    response = json_util.dumps(document)
    return Response(response, mimetype='application/json')


# Create a route that allows you to list all characters
@app.route('/lotr_characters/char/<char>', methods=['GET'])
def get_characters(char):
    document = ft.get_documents(mongo=mongo, key='char', value=char)
    if not document:
        return not_found()

    response = json_util.dumps(document)
    return Response(response, mimetype='application/json')


# Create a path that allows the sentiment analysis of a dialogue
@app.route('/lotr_characters/sa/<_id>', methods=['GET'])
def get_analysis(_id):
    document = ft.get_analysis(mongo=mongo, _id=_id)
    if not document:
        return not_found()

    response = json_util.dumps(document)
    return Response(response, mimetype='application/json')


# Create a route that allows you to delete document
@app.route('/lotr_characters/<_id>', methods=['DELETE'])
def delete_document(_id):
    ft.delete_document(mongo=mongo, _id=_id)
    response = jsonify({'message': 'Document ' + _id + ' was deleted successfully'})
    return response


# Create a route to update documents
@app.route('/lotr_characters/<_id>', methods=['PUT'])
def update_document(_id):
    char = request.json['char']
    dialog = request.json['dialog']
    movie = request.json['movie']

    if char and dialog and movie:
        ft.update_document(mongo, _id, char, dialog, movie)
        response = jsonify({'massage': 'Document ' + _id + ' was updated successfully'})
        return response

# Handling Errors
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404

    return response


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    #app.run(debug=True)
    app.run("0.0.0.0", 5001, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
