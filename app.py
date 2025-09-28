import random
import string
# Add 'flash' to the import list
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# A secret key is required to use the flashing system
app.config['SECRET_KEY'] = 'a-very-secret-and-random-string' 

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
    
    # Flash the success message before redirecting
    flash('Note created successfully! You can now share this link.')
    
    return redirect(url_for('view_note', note_id=note_id))

@app.route('/note/<note_id>')
def view_note(note_id):
    note_content = notes_database.get(note_id)
    if note_content is not None:
        return render_template('view_note.html', note_content=note_content)
    else:
        return "Note not found.", 404

if __name__ == '__main__':
    app.run(debug=True)