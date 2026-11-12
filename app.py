
from flask import Flask, render_template, request

# Import phishing detection function
from detector import analyze_email

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Analyze email
@app.route("/analyze", methods=["POST"])
def analyze():

    email = request.form.get("email_content", "")

    sender_email = request.form.get("sender_email", "")

    result = analyze_email(email, sender_email)

    # Display results
    return render_template(
    "result.html",
    email=email,
    sender_email=sender_email,
    result=result
    )

# Run application
if __name__ == "__main__":
    app.run(debug=True)
