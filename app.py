from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Replace the URI with your MongoDB server URI
client = MongoClient('mongodb://localhost:27017/')
db = client['userDB']
users_collection = db['users']

@app.route('/')
def index():
    return render_template('land-page.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/create-group')
def create_group():
    return render_template('create-group.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/join-group')
def join_group():
    return render_template('join-group.html')

@app.route('/new-hobbie-group')
def new_hobbie_group():
    return render_template('new-hobbie-group.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    username = data.get('username')
    password = data.get('password')
    degree = data.get('degree')
    yearofstudy = data.get('yearofstudy')

    if not all([firstname, lastname, username, password, degree, yearofstudy]):
        return jsonify({"error": "Missing required fields"}), 400

    hashed_password = generate_password_hash(password)
    user = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password": hashed_password,
        "degree": degree,
        "yearofstudy": yearofstudy
    }

    if users_collection.find_one({"username": username}):
        return jsonify({"error": "User already exists"}), 400

    users_collection.insert_one(user)
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/perform-login', methods=['POST'])
def perform_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users_collection.find_one({"username": username})
    if user and check_password_hash(user['password'], password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401
    
if __name__ == '__main__':
    app.run(debug=True)
