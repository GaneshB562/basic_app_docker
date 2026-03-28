from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)')
    conn.commit()
    conn.close()

@app.route('/notes', methods=['GET'])
def get_notes():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM notes')
    notes = c.fetchall()
    conn.close()
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('INSERT INTO notes (text) VALUES (?)', (data['text'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Note added"})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
