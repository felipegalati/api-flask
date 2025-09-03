from flask import Flask, jsonify, request
app = Flask(__name__)
# USUARIOS
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "user não encontrado"}), 404


@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    if not new_user or 'name' not in new_user:
        return jsonify({"message": "Dados inválidos"}), 400
        
    
    new_user['id'] = len(users) + 1 
    users.append(new_user)
    return jsonify(new_user), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user.update(user_data)
        return jsonify(user)
    return jsonify({"message": "user não encontrado"}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    original_len = len(users)
    users = [user for user in users if user['id'] != user_id]
    if len(users) < original_len:
        return jsonify({"message": "user deletado com sucesso"}), 200
    return jsonify({"message": "user não encontrado"}), 404