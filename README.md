
# MailShield – Email Security Analyzer

MailShield is a Python Flask-based web application that analyzes email content and identifies suspicious indicators that may be associated with phishing attacks.

## Project Overview

The application examines email content and sender information using rule-based detection techniques. It calculates a risk score and classifies the email as Low Risk, Medium Risk, or High Risk.

## Features

- Suspicious phrase detection
- URL detection
- Shortened URL identification
- IP-based URL detection
- Sender domain analysis
- Punycode domain detection
- Risk score calculation
- Risk level classification
- Recommended security actions
- Detailed detection findings

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Regular Expressions

## Project Structure

MailShield/
- app.py
- detector.py
- templates/
- static/
- requirements.txt
- README.md

## How It Works

1. User enters the sender email address.
2. User pastes the email content.
3. MailShield analyzes the submitted information.
4. The detection engine calculates a risk score.
5. The application displays the risk level and findings.

## Risk Classification

- Low Risk: Score below 2
- Medium Risk: Score from 2 to 3
- High Risk: Score 4 or above

## Installation and Setup

1. Clone the repository.
2. Install the required dependencies:

   pip install -r requirements.txt

3. Run the application:

   python app.py

4. Open the browser:

   http://127.0.0.1:5000/

## Disclaimer

MailShield is an educational security analysis prototype. Its rule-based checks cannot guarantee that an email is safe or malicious. Always verify suspicious messages independently.
