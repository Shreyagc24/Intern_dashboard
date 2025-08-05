from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# Get MongoDB URI securely from environment variable (do not hardcode)
MONGO_URI = os.environ.get("MONGO_URI")
if not MONGO_URI:
    raise Exception("MONGO_URI environment variable not set")

# MongoDB Setup
client = MongoClient(MONGO_URI)
db = client['intern_dashboard']
interns = db['interns']

# Dummy Data Insert (only once if empty)
if interns.count_documents({}) == 0:
    interns.insert_many([
        {"name": "Ritik", "referral": "ritik2025", "donation": 1200},
        {"name": "Shreya", "referral": "shreya2025", "donation": 1200},
        {"name": "Krishna", "referral": "krishna2025", "donation": 850},
        {"name": "Ajay", "referral": "ajay2025", "donation": 1000},
    ])

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('dashboard', username=username))
    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    intern = interns.find_one({'name': username.capitalize()})
    if not intern:
        return "Intern not found!", 404
    return render_template('dashboard.html', intern=intern)

@app.route('/api/intern/<username>')
def get_intern_data(username):
    intern = interns.find_one({'name': username.capitalize()})
    if not intern:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "name": intern['name'],
        "referral": intern['referral'],
        "donation": intern['donation']
    })

@app.route('/leaderboard')
def leaderboard():
    data = list(interns.find().sort("donation", -1))
    return render_template('leaderboard.html', data=data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
