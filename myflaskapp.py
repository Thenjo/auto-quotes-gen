from flask import Flask, render_template,jsonify
import json
import random
app=Flask(__name__)
@app.route('/api/quote')
def display():
    with open('quotes.json') as json_file:
        data = json.load(json_file)
        res=random.randint(0,len(data))
        d = render_template('index.html')
    return (data[res]["quote"],d)
if __name__=='__main__':
    app.run(host='localhost', port=8008)
