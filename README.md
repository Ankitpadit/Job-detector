# Job-detector

# 🛡️ AI-Based Job Scam Detection System

A real-time web application that analyzes job descriptions and detects potential job scams using NLP-based heuristic rules and risk scoring.

---

## 📌 Problem Statement

Job scams targeting students and freshers have increased rapidly.  
Fake job postings often promise high salaries, no interviews, or ask for fees through WhatsApp or Telegram.

Most users realize the fraud only **after losing money or personal data**.

---

## 🎯 Objective

- Analyze job descriptions in real time  
- Detect scam patterns and red flags  
- Provide a scam risk score (0–100%)  
- Classify job posts as:
  - **Likely Real**
  - **Suspicious**
  - **Fake**
- Provide explainable reasons for detection  

---

## ⚙️ How It Works

1. User pastes a job description  
2. Text is analyzed using NLP-based rules  
3. Scam indicators and positive signals are detected  
4. A weighted risk score is calculated  
5. Final classification is displayed with explanations  

---

## 🧠 Detection Logic

### 🔴 Negative Signals
- Urgency language (e.g., *urgent hiring*)
- No interview process
- WhatsApp / Telegram hiring
- Unrealistic salary promises
- Fee or registration requests

### 🟢 Positive Signals
- Company name mentioned
- Interview process defined
- Professional email address
- Clear job responsibilities
- Location specified

Hard red flags like **fee requests** or **no interview** are weighted heavily to reduce false negatives.

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – Web application framework
- **Regular Expressions (Regex)** – Pattern detection
- **NLP Heuristic Rules**
- **Risk Scoring Model**

---

## 🚀 Features

- Real-time job scam detection
- Scam risk score (0–100%)
- Clear classification: Real / Suspicious / Fake
- Highlighted scam indicators
- Clean and professional UI
- Explainable output (not black-box AI)

---

## 🌍 Real-World Applications

- Students and freshers avoiding job scams
- College placement cells (TPO)
- Job portals for filtering fake postings
- Cyber safety and fraud awareness tools

---

## ⚠️ Limitations

- Works on text-based analysis only
- Cannot verify company authenticity externally
- Provides risk assessment, not absolute verification

---

## 🔮 Future Enhancements

- Machine learning model trained on real datasets
- Browser extension for live job checking
- API integration with job portals
- Multilingual job description analysis
- User feedback-based learning

---

## ▶️ How to Run the Project

```bash
pip install streamlit
streamlit run app.py
