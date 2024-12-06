from flask import Flask, render_template, request, jsonify
import random
import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Data storage simulation (to replace with a database later)
data_store = {
    "users": [],
    "observations": [],
    "ai_feedback": [],
}

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# User onboarding route
@app.route('/onboard', methods=['POST'])
def onboard():
    user_data = request.json
    user_data["user_id"] = len(data_store["users"]) + 1
    data_store["users"].append(user_data)
    return jsonify({"message": "User onboarded successfully", "user_id": user_data["user_id"]})

# Observation input route
@app.route('/observe', methods=['POST'])
def observe():
    observation = request.json
    observation["timestamp"] = datetime.datetime.now().isoformat()
    data_store["observations"].append(observation)
    return jsonify({"message": "Observation recorded", "observation": observation})

# AI feedback route
@app.route('/ai_feedback', methods=['POST'])
def ai_feedback():
    feedback_data = request.json
    feedback_data["response"] = generate_ai_response(feedback_data["input"])
    data_store["ai_feedback"].append(feedback_data)
    return jsonify(feedback_data)

# Generate AI response (dummy function)
def generate_ai_response(user_input):
    responses = [
        "Based on your input, consider reviewing your diet and sleep schedule.",
        "It may help to monitor stress levels and ensure hydration.",
        "Your observations suggest a potential pattern in your health cycles.",
    ]
    return random.choice(responses)

# AI assistant: question for the day
@app.route('/question_of_the_day')
def question_of_the_day():
    questions = [
        "What was your energy level like today?",
        "Did you notice any unusual symptoms after meals?",
        "How many hours of sleep did you get last night?",
    ]
    return jsonify({"question": random.choice(questions)})

# Personalized advice route
@app.route('/daily_advice/<user_id>')
def daily_advice(user_id):
    advice = {
        "diet": "Increase fiber intake for better digestion.",
        "exercise": "Consider a light 30-minute walk today.",
        "hydration": "Aim for at least 8 glasses of water.",
    }
    return jsonify({"user_id": user_id, "advice": advice})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
