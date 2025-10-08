# Note Sharer - A Full-Stack Web Application

A full-stack web application built with Flask and MongoDB. This application allows users to register, log in, and create private, text-based notes. Each note can also be shared publicly via a unique, randomly generated link. This project demonstrates a complete user authentication system, persistent cloud database integration, and a responsive frontend.

---
## Live Demo

You can view the live, deployed application here:
**[https://my-note-sharer.onrender.com](https://my-note-sharer.onrender.com)**

---
## Features

* **User Registration & Login**: Secure user authentication system with password hashing.
* **Persistent Storage with MongoDB**: User and note data is stored permanently in a MongoDB Atlas cloud database.
* **User-Specific Notes**: A private "My Notes" section where logged-in users can view and manage their own notes.
* **Public Note Sharing**: Each created note has a unique URL that can be shared publicly for viewing.
* **Responsive Frontend**: The user interface is built with Bootstrap 5 to be functional on both desktop and mobile devices.

---
## 🛠️ Technologies Used

* **Backend**: Python, Flask, Flask-Login, Werkzeug (for password hashing), Gunicorn
* **Frontend**: HTML, Bootstrap 5, jQuery
* **Database**: MongoDB Atlas, PyMongo
* **Deployment**: Render, Git & GitHub

---
##  Local Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-github-repo-url>
    cd note-sharer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project folder and add your environment variables.
    ```
    MONGO_URI="your_mongodb_connection_string"
    ```

5.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

---


