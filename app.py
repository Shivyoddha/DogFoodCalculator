!pip install flask
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def calculate_food(activity, weight):
    if activity and weight:
        calculated_amount = round(activity / weight, 2)
        return {"recommendedFood": calculated_amount}
    else:
        return {"error": "Please provide both activity level and weight."}

@app.route('/calculate_food', methods=['POST'])
def calculate_food_api():
    try:
        data = request.get_json()
        activity = data.get("activity")
        weight = data.get("weight")
        result = calculate_food(activity, weight)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
