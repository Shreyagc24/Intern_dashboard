# 🚀 Intern Dashboard

A simple full-stack web app to manage intern profiles, track referral codes, and display donations and rewards. Built with **Flask**, **MongoDB**, and styled with CSS, this project showcases CRUD operations, REST API integration, and frontend-backend communication.

## ✨ Features

- Dummy login/signup page (no real authentication)
- 📊 Dashboard displaying:
  - Intern name
  - Total donations raised
  - Rewards/unlockables section (static)
- Leaderboard page listing interns by total donations
- REST API endpoints serving intern data (JSON)
- MongoDB integration for data persistence


## 🛠️ Tech Stack

- **Backend:** Python, Flask 🐍
- **Database:** MongoDB 
- **Frontend:** HTML, CSS, Jinja2 templates
- **Tools:** Git, VS Code, Render


## 📁 Project Structure


intern\_dashboard/
│
├── app.py               # Flask backend app
├── requirements.txt     # Python dependencies
├── static/
│   └── style.css        # CSS styling
└── templates/
├── login.html       # Login page template
├── dashboard.html   # Dashboard page template
└── leaderboard.html # Leaderboard page template

## ⚙️ Installation & Setup

1. Clone the repo:
bash
git clone https://github.com/Shreyagc24/Intern_dashboard.git
cd Intern_dashboard


2. Create and activate a Python virtual environment:
bash
python -m venv venv
### Windows
venv\Scripts\activate
### Linux/macOS
source venv/bin/activate

3. Install dependencies:
bash
pip install -r requirements.txt

4. Start MongoDB locally or use a service like MongoDB Compass.

5. Run the Flask app:
bash
python app.py

6. Open your browser and go to Render Live link

## 📜 License
MIT License © 2025 Shreya Garg