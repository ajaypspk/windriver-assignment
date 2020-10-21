#!/usr/bin/python
import json
from flask import Flask,  jsonify, request
import requests
import base64

app = Flask(__name__)

def api_response(input='', output='', status='success', msg=''):
    return jsonify(
        {
            "input": input,
            "output": output,
            "status": status,
            "message": msg
        }
    )

@app.route('/api/health', methods=['GET'])
def ping():
    try:
        return api_response(output="ok")
    except Exception as e:
        raise e

@app.route('/api/encrypt', methods=['GET'])
def encrypt():
    try:
        data = request.get_json()
        if not data:
            return  api_response(msg="request body is missing", status="error"), 400
        if not data.get("input") :
            return  api_response(msg="input request parameter is missing", status="error"), 400
        
        input = data.get('input')
        output = base64.b64encode(input.encode("utf-8")).decode('utf-8')
        return api_response(input=input,output=output)
    except Exception as e:
        raise e

@app.route('/api/decrypt', methods=['GET'])
def decrypt():
    input = None
    try:
        data = request.get_json()
        if not data:
            return  api_response(msg="request body is missing", status="error"), 400
        if not data.get("input") :
            return  api_response(msg="input request parameter is missing", status="error"), 400
        
        input = data.get('input')

        output = base64.b64decode(input.encode("utf-8")).decode('utf-8')
        return api_response(input=input,output=output)
    except Exception as e:
        return api_response(input=input,status="error", msg=str(e)), 400


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug = True)