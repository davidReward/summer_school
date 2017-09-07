from flask import Flask, jsonify, abort, make_response, url_for, request, Response
from flask.ext.httpauth import HTTPBasicAuth
from sss_db import *
from flask_cors import CORS, cross_origin
from sss_config import *
import sys
import json

auth = HTTPBasicAuth()

app = Flask(__name__)
CORS(app,supports_credentials=True)


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



@app.route('/api/signer', methods=['GET', 'POST'])
#@auth.login_required
def json_in_db():
    # force erzwingt interpretation als JSON
    content = request.get_json(force=True)

    # TODO: Daten loeschen mit where 1 cond.

    for item in range(0,len(content)):
        writeDB(content[item]['Name'], 'no position', 'no description', content[item]['Timespan'] , content[item]['URL'])

    #writeDB(content[0]['Name'], 'keine Position', 'keine Beschreibung', content[0]['Timespan'])


    resp = jsonify()
    resp.status_code = 201
    return resp


@app.route('/api/signer/<string:name>', methods=['GET'])
#@auth.login_required
def json_from_db(name):
    query_result = readDB(name)
    if len(query_result) != 0:
        return jsonify({'signers': query_result})


    abort(404)

@app.route('/api/signers', methods=['GET'])
#@auth.login_required
def json_from_db_all():
    query_result = readDB_all()
    if len(query_result) != 0:
        return jsonify({'signers': query_result})
    abort(404)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)


