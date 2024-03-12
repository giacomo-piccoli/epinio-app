from flask import jsonify, request
from app import app

# Sample data - list of items
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Route to get a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# Route to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = {'id': len(items) + 1, 'name': data['name']}
    items.append(new_item)
    return jsonify(new_item), 201

# Route to update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item['name'] = data['name']
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# Route to delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})
