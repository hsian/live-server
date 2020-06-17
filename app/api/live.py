from flask import jsonify, request, g
from urllib import parse
from . import api

@api.route('/client_connect/', methods=['get','post'])
def test():
    # pass
    return '0'

@api.route('/client_publish/', methods=['get','post'])
def client_connect():
    url = request.json.get("param")
    result = parse.urlparse(url)
    query_dict = parse.parse_qs(result.query)
    token = query_dict.get('token', [None])[0]
    if (token is None) and (token != '123456'):
        return '1'
    return '0'

