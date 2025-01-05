from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Helper function to interpret BMI
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate_bmi", methods=["POST"])
def calculate_bmi():
    try:
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        
        if weight <= 0 or height <= 0:
            return jsonify({"error": "Invalid input. Weight and height must be greater than zero."}), 400
        
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        desc = interpret_bmi(bmi)

        return jsonify({
            "bmi": round(bmi, 2),
            "desc": desc
        })
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter numeric values."}), 400

if __name__ == "__main__":
    app.run(debug=True)
