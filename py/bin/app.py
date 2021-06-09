from flask import Flask, jsonify
from prometheus_client import Counter

view_metric = Counter('view', 'Product view')

app = Flask(__name__)

greeting = {"message": "hello world"}

@app.route('/')
def hello():
    view_metric.inc()
    return jsonify(greeting)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
