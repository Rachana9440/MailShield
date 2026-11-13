# 🛡️ MailShield – Email Security Analyzer

<p align="center">
  A Python Flask-based web application for identifying suspicious email indicators and assessing potential phishing risks.
</p>

<p align="center">
  ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
  ![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
  ![HTML](https://img.shields.io/badge/HTML-Frontend-orange?logo=html5)
  ![CSS](https://img.shields.io/badge/CSS-Styling-blue?logo=css3)
  ![Security](https://img.shields.io/badge/Domain-Cybersecurity-green)
</p>

---

## 📌 Project Overview

**MailShield** is a beginner-friendly email security analysis application developed using Python and Flask.

It examines email content and sender information using rule-based detection techniques to identify suspicious indicators commonly associated with phishing attacks.

The application calculates a risk score, classifies the email into a risk category, and provides security recommendations to help users understand potential threats.

## ✨ Features

- 🔍 Suspicious phrase detection
- 🔗 URL detection and analysis
- ⚠️ Shortened URL identification
- 🌐 IP-based URL detection
- 📧 Sender domain analysis
- 🔤 Punycode domain detection
- 📊 Risk score calculation
- 🚦 Risk level classification
- 🛡️ Recommended security actions
- 📋 Detailed detection findings

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Backend web framework |
| HTML | Web page structure |
| CSS | User interface styling |
| Regular Expressions | Pattern-based detection |

## 📂 Project Structure

```text
MailShield/
│
├── static/
│   └── css/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── detector.py
├── requirements.txt
├── Start_MailShield.bat
├── .gitignore
└── README.md
```

## ⚙️ How It Works

1. The user enters the sender's email address.
2. The user pastes the email content.
3. MailShield examines the submitted information.
4. The detection engine searches for suspicious indicators.
5. A risk score is calculated based on the detected indicators.
6. The application displays the risk category, findings, and recommended security actions.

## 🚦 Risk Classification

| Risk Level | Risk Score |
|---|---|
| 🟢 Low Risk | Below 2 |
| 🟡 Medium Risk | 2 to 3 |
| 🔴 High Risk | 4 or above |

## 📸 Screenshots

*Add screenshots of your actual running application below.*

### 🏠 Home Page

![MailShield Home Page](screenshots/home.png)

### 📊 Email Analysis Result

![MailShield Analysis Result](screenshots/result.png)

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rachana9440/MailShield.git
```

### 2. Open the project folder

```bash
cd MailShield
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

### 4. Activate the virtual environment on Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in your browser

Visit:

http://127.0.0.1:5000/

## 🎯 Project Objective

The objective of MailShield is to demonstrate how basic cybersecurity concepts and rule-based detection techniques can be applied to identify suspicious email characteristics through a simple web application.

## ⚠️ Disclaimer

MailShield is an educational security analysis prototype. Its rule-based detection techniques cannot guarantee that an email is safe or malicious. The results are intended to provide preliminary security indicators, not a definitive verdict. Always verify suspicious messages independently.

---

<p align="center">
  <b>Developed as a Cybersecurity Learning Project</b>
</p>
