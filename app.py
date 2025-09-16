from flask import Flask, jsonify, request
from flask_cors import CORS

# from src.model.agenda import ( get_agenda  )
# from src.model.users import ( get_users)
# import agenda

from src.model import agenda 
from src.model import users , itens
# import users
 #http://192.168.13.191:5000/agenda
 
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

# Mapeamento de rotas
route_map = {
    'agenda': agenda,
    'users': users,
    'produtos': itens
}

# autentica o usuario
# @app.route('/<resource>/auth', methods=["POST"])
# def auth(resource):
#     return users.auth()

@app.route('/<resource>', methods=["GET", "POST"])
@app.route('/<resource>/<int:id>', methods=["GET", "PUT", "DELETE"])
def handle_resource(resource, id=None):
    if resource in route_map:
        if request.method == "GET":
            if id is not None:
                return route_map[resource].getBy(id)    
            return route_map[resource].get()        
        elif request.method == "POST":
            return route_map[resource].post()
        elif request.method == "PUT":
            return route_map[resource].put(request.args.get(id))
        elif request.method == "DELETE":
            return route_map[resource].delete(request.args.get(id))
    return jsonify({"error": "Resource not found"}), 404

# @app.route('/agenda', methods=['GET'])
# def get_all_agenda_items():
#     return get_agenda()

# @app.route('/users', methods=['GET'])
# def get_all_users():
#     return get_users()

if __name__ == '__main__':
    app.run(debug=True) # debug=True para desenvolvimento