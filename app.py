from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (initial contacts)
contacts = [
    {
        "id": 1,
        "name": "John Doe",
        "phone": "1234567890",
        "email": "johndoe@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "phone": "9876543210",
        "email": "janesmith@example.com"
    }
]

# Get all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

# Get a contact by ID
@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    for contact in contacts:
        if contact['id'] == contact_id:
            return jsonify(contact)
    return jsonify({"message": "Contact not found"}), 404

# Create a new contact
@app.route('/contacts', methods=['POST'])
def create_contact():
    new_contact = {
        "id": len(contacts) + 1,
        "name": request.json.get('name'),
        "phone": request.json.get('phone'),
        "email": request.json.get('email')
    }
    contacts.append(new_contact)
    return jsonify(new_contact), 201

# Update a contact
@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    for contact in contacts:
        if contact['id'] == contact_id:
            contact['name'] = request.json.get('name')
            contact['phone'] = request.json.get('phone')
            contact['email'] = request.json.get('email')
            return jsonify(contact)
    return jsonify({"message": "Contact not found"}), 404

# Delete a contact
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    for contact in contacts:
        if contact['id'] == contact_id:
            contacts.remove(contact)
            return jsonify({"message": "Contact deleted"})
    return jsonify({"message": "Contact not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

