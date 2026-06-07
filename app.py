from flask import Flask, render_template, request, jsonify
import random
import os
import json

app = Flask(__name__)
SAVE_FILE = "arise_save_data.json"

QUEST_BANK = [
    {"id": 1, "title": "Demon Back Awakening", "tasks": ["4x Max Pull-ups", "4x10 Dumbbell Rows", "3x12 Barbell Shrugs"], "xp": 150},
    {"id": 2, "title": "Boulder Shoulders", "tasks": ["4x8 Barbell Overhead Press", "4x15 Dumbbell Lateral Raises", "3x12 Front Raises"], "xp": 120},
    {"id": 3, "title": "Chest Expansion", "tasks": ["4x10 Dumbbell Bench Press", "4x12 Dumbbell Flyes", "3x Max Push-ups"], "xp": 130}
]

def load_player_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r') as file:
            return json.load(file)
    return {"level": 1, "xp": 0, "xp_to_next_level": 500, "streak": 0, "total_workouts": 0}

def save_player_data(data):
    with open(SAVE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def home():
    data = load_player_data()
    # Pick a random quest for the session
    quest = random.choice(QUEST_BANK)
    return render_template('index.html', data=data, quest=quest)

@app.route('/complete_quest', methods=['POST'])
def complete_quest():
    data = load_player_data()
    req = request.get_json()
    
    status = req.get('status')
    xp_reward = req.get('xp_reward', 0)

    if status == 'success':
        data['xp'] += xp_reward
        data['streak'] += 1
        data['total_workouts'] += 1
        
        # Level up logic
        while data['xp'] >= data['xp_to_next_level']:
            data['level'] += 1
            data['xp'] -= data['xp_to_next_level']
            data['xp_to_next_level'] = int(data['xp_to_next_level'] * 1.5)
    elif status == 'fail':
        data['streak'] = 0

    save_player_data(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
