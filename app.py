from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def get_items():
        return jsonify({"messaage": "ola mundo"})

if __name__ == '__main__':
        app.run(debug=True)