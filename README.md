# 🛡️ PhishGuard AI: Advanced Cybersecurity Threat Scanner

> An intelligent, real-time phishing URL detection and threat analysis system powered by Machine Learning and Heuristic Feature Extraction.

---

## 🚀 Overview
**PhishGuard AI** is a lightweight security tool designed to instantly detect malicious phishing links and social engineering vectors. Instead of relying on static blacklists, it analyzes structural and behavioral URL properties using a supervised machine learning classifier to evaluate threats in real time.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn (`RandomForestClassifier`)
* **Data Processing & Heuristics:** Pandas, Regular Expressions (`re`)
* **User Interface:** Gradio (Interactive Web Dashboard)

---

## 🔍 Key Heuristic Features Extracted
1. **URL Length:** Identifies abnormal string lengths used to obscure domains.
2. **IP Address Detection:** Flags raw numeric IP addresses (e.g., `192.168.x.x`) used instead of proper domain names.
3. **Redirection Tricks:** Detects `@` symbol routing manipulation.
4. **URL Shorteners:** Flags high-risk redirection services (`bit.ly`, `t.co`, etc.).
5. **High-Risk Keywords:** Scans for social engineering urgency terms (`login`, `verify`, `banking`, `secure`, `update`).
6. **Structural Checks:** Evaluates dot (`.`) nesting and secure HTTPS protocol compliance.

---

## ⚙️ Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/PhishGuard-AI-Scanner.git](https://github.com/YourUsername/PhishGuard-AI-Scanner.git)
   cd PhishGuard-AI-Scanner
   
