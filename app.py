from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import uuid

app = Flask(__name__)

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client['intern_dashboard']
interns = db['interns']

# Dummy Data Insert (only runs once)
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
    app.run(debug=True)
