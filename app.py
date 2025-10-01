import os
import random
import string
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from dotenv import load_dotenv
from user import User

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "a-default-fallback-secret-key")


MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.get_database("note_sharer_db")
notes_collection = db.get_collection("notes")
users_collection = db.get_collection("users")

# --- Flask-Login Setup ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Redirect to login page if user is not authenticated

@login_manager.user_loader
def load_user(user_id):
    user_data = users_collection.find_one({'_id': ObjectId(user_id)})
    if user_data:
        return User(user_data)
    return None

# --- Helper Functions ---
def generate_note_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# --- Public Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/note/<note_id>')
def view_note(note_id):
    note = notes_collection.find_one({"note_id": note_id})
    if note:
        return render_template('view_note.html', note_content=note['content'])
    else:
        return "Note not found.", 404

# --- Authentication Routes ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        existing_user = users_collection.find_one({'email': email})
        if existing_user:
            flash('Email address already exists.')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        users_collection.insert_one({'email': email, 'password': hashed_password})
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_data = users_collection.find_one({'email': email})
        
        if user_data and check_password_hash(user_data['password'], password):
            user = User(user_data)
            login_user(user)
            return redirect(url_for('my_notes'))
        else:
            flash('Invalid email or password.')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# --- Protected Routes (User must be logged in) ---
@app.route('/create', methods=['POST'])
@login_required
def create_note():
    note_content = request.form.get('note_content')
    note_id = generate_note_id()
    
    notes_collection.insert_one({
        "note_id": note_id,
        "content": note_content,
        "user_id": ObjectId(current_user.id)
    })
    
    flash('Note created successfully! You can now share this link.')
    return redirect(url_for('view_note', note_id=note_id))

@app.route('/my-notes')
@login_required
def my_notes():
    user_notes = notes_collection.find({"user_id": ObjectId(current_user.id)})
    return render_template('my_notes.html', notes=user_notes)

if __name__ == '__main__':
    app.run(debug=True)