from flask import Flask, render_template

app = Flask(__name__)

person = {
    "name": "Sundar D",
    "age": 21,
    "phone": "8925392555",
    "problem": "Temple bald area (sotta)",
    "hospital": "Hair Transplant Clinic",
    "cost_per_graft": "₹35",
    "required_grafts": "800"
}

@app.route("/")
def home():
    return render_template("index.html", person=person)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)