from flask import Flask, jsonify, request, g
from werkzeug.security import generate_password_hash, check_password_hash
import database

app = Flask(__name__)

# Create a new note
@app.route('/notes', methods=['POST'])
def create_note():
    db = database.get_db()
    cursor = db.cursor()
    title = request.json.get('title')
    content = request.json.get('content')
    note_type = request.json.get('type')

    cursor.execute('INSERT INTO notes (title, content, type) VALUES (?, ?, ?)',
                   (title, content, note_type))
    db.commit()

    return jsonify({'message': 'Note created successfully'})

# Retrieve all notes
@app.route('/notes', methods=['GET'])
def get_all_notes():
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()

    notes_list = []
    for note in notes:
        note_dict = {
            'id': note[0],
            'title': note[1],
            'content': note[2],
            'type': note[3]
        }
        notes_list.append(note_dict)

    return jsonify(notes_list)

# Default route
@app.route('/')
def default_route():
    return 'Welcome to the note storage system'

if __name__ == '__main__':
    database.init_db(app)  # Initialize the database
    app.run(debug=True)
