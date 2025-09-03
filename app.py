from flask import Flask, jsonify, request
from src.model.agenda import ( get_agenda )

app = Flask(__name__)

@app.route('/agenda/<int:item_id>', methods=['GET'])
def get_all_agenda_items():
        return get_agenda()

if __name__ == '__main__':
    app.run(debug=True)