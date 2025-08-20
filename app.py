from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
        {"id": 1, "name": "Item A", "description": "Descrição do Item A"},
        {"id": 2, "name": "Item B", "description": "Descrição do Item B"},
]

users = [
        {"id": 1, "name": "José", "password": "1234"},
        {"id": 2, "name": "Maria", "password": "5678"},
]

# ITENS
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404


@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    if not new_item or 'name' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    
    new_item['id'] = len(items) + 1 
    items.append(new_item)
    return jsonify(new_item), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item_data = request.json
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items 
    original_len = len(items)
    items = [item for item in items if item['id'] != item_id]
    if len(items) < original_len:
        return jsonify({"message": "Item deletado com sucesso"}), 200
    return jsonify({"message": "Item não encontrado"}), 404


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



if __name__ == '__main__':
    app.run(debug=True)