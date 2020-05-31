from flask import jsonify, request, g
from . import api

@api.route('/test/', methods=['get','post'])
def test():
    print('444')
    return '0'

@api.route('/client_connect/', methods=['get','post'])
def client_connect():
    print('123123123123123')
    return '0'
