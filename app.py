import random
import string
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes_database = {}

def generate_note_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_note():
   
    note_content = request.form.get('note_content')
    
    
    note_id = generate_note_id()
    
   
    notes_database[note_id] = note_content
    

    return redirect(url_for('view_note', note_id=note_id))

@app.route('/note/<note_id>')
def view_note(note_id):
    return f"This will be the page for note {note_id}"

if __name__ == '__main__':
    app.run(debug=True)