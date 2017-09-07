from flask import Flask, jsonify, abort, make_response, url_for, request, Response
from flask.ext.httpauth import HTTPBasicAuth
from db import *
from flask_cors import CORS, cross_origin
from config import *
import sys
import json

auth = HTTPBasicAuth()

app = Flask(__name__)
CORS(app,supports_credentials=True)


def make_public_mdatum(mdata):
    new_ressource = {}
    for field in mdata:
        if field == 'id':
            new_ressource['uri'] = url_for('get_mdatum', mdatum_id=mdata['id'], _external=True)
        else:
            new_ressource[field]= mdata[field]
    return new_ressource
	
def minimizeData(query_result):
    query_result_New = query_result
    
    return query_result_New


@auth.get_password
def get_password(username):
    if username == USERNAME:
        return PASSWORD
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Kein Name gefunden'}), 404)



@app.route('/api/insert', methods=['GET', 'POST'])
@auth.login_required
def json_in_db():
    # force erzwingt interpretation als JSON
    content = request.get_json(force=True)

    # TODO: Daten loeschen mit where 1 cond.

    for item in range(0,len(content)):
        writeDB(content[item]['Name'], 'keine Position', 'keine Beschreibung', content[item]['Timespan'])

    #writeDB(content[0]['Name'], 'keine Position', 'keine Beschreibung', content[0]['Timespan'])


    resp = jsonify()
    resp.status_code = 201
    return resp


@app.route('/api/signer', methods=['GET'])
def json_from_db():
    # force erzwingt interpretation als JSON

    print readDB('ram potty')



    resp = jsonify()
    resp.status_code = 201
    return resp


if __name__ == '__main__':

    print readDB("amouda")
    #app.run(host='0.0.0.0',port=8080, debug=True)


