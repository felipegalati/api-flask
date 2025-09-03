from flask import Flask, jsonify, request
app = Flask(__name__)
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