from flask import Flask, jsonify
import requests
import argparse

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return "Hi, This code is develop by Prakash Kumar: 1", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
