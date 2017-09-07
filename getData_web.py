from flask import Flask, jsonify, abort, make_response, url_for, request
from flask.ext.httpauth import HTTPBasicAuth
from createJSON import *
from flask_cors import CORS, cross_origin
from config import *

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



@app.route('/api/insert', methods=['GET'])
@auth.login_required
def get_mdataUnit(name, pos, description, date):
    name = request.args.get('begin')
    end = request.args.get('end')
    anzahlDatenpunkte =  request.args.get('anzahl')

    if begin is not None and end is not None:
        query_result = queryDB_station_interval(station, unit, begin, end)
        query_result =  minimizeData(query_result)
        if len(query_result) != 0:
            return jsonify({'Messdaten':  [make_public_mdatum(data) for data in query_result]})

    abort(404)

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=8080, debug=True)
    testDB('DUMPer', '8', 'blablup', 'Sept')