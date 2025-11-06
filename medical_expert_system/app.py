from flask import Flask, render_template, request

app = Flask(__name__)

# Knowledge base (symptoms -> possible diseases)
knowledge_base = {
    "Common Cold": {"symptoms": {"cough", "sneezing", "runny nose"}, "cf": 0.9},
    "Flu": {"symptoms": {"fever", "cough", "fatigue", "chills"}, "cf": 0.95},
    "COVID-19": {"symptoms": {"fever", "cough", "fatigue", "loss of smell"}, "cf": 0.98},
    "Allergy": {"symptoms": {"sneezing", "itchy eyes", "runny nose"}, "cf": 0.85},
    "Malaria": {"symptoms": {"fever", "chills", "sweating", "headache"}, "cf": 0.9}
}

def diagnose(symptoms):
    symptoms = {s.lower().strip() for s in symptoms}
    results = []
    for disease, data in knowledge_base.items():
        disease_symptoms = {s.lower() for s in data["symptoms"]}
        matches = len(symptoms & disease_symptoms)
        total = len(disease_symptoms)
        confidence = (matches / total) * data["cf"]
        if matches > 0:
            results.append((disease, round(confidence * 100, 2)))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    user_input = request.form["symptoms"]
    symptoms = user_input.split(",")
    diagnosis = diagnose(symptoms)
    return render_template("result.html", user_input=user_input, diagnosis=diagnosis)

if __name__ == "__main__":
    app.run(debug=True)
