from flask import Flask, jsonify
from bingobingo_playground import fetch_bingobingo_to_database, predict_hangod
app = Flask(__name__)

@app.route('/predict_hangod')
def predict():
    newest_identity, newest_pred = predict_hangod()
    return jsonify(response="OK",
        newest_identity=str(newest_identity),
        newest_pred=bool(newest_pred[0]))

@app.route('/fetch')
def fetch():
    fetch_bingobingo_to_database()
    return jsonify(response="OK")

if __name__ == '__main__':
    app.run()

application = app
