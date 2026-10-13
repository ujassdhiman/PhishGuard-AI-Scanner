import gradio as gr
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import re

# Step 1: Heuristic Feature Extraction Engine
def extract_advanced_features(url):
    length = len(url)
    
    # Check for IP address
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    has_ip = 1 if ip_pattern.search(url) else 0
    
    # Check for '@' symbol redirection
    has_at = 1 if "@" in url else 0
    
    # Check for URL shorteners
    shorteners = ["bit.ly", "t.co", "goo.gl", "tinyurl.com", "ow.ly", "is.gd"]
    has_shortener = 1 if any(short in url.lower() for short in shorteners) else 0
    
    # Check for high-risk keywords
    keywords = ["login", "verify", "update", "account", "secure", "signin", "banking", "confirm"]
    suspicious_keyword = 1 if any(kw in url.lower() for kw in keywords) else 0
    
    # Structural counts
    dot_count = url.count(".")
    has_https = 1 if url.startswith("https") else 0
    
    return [length, has_ip, has_at, has_shortener, suspicious_keyword, dot_count, has_https]

# Step 2: Training Dataset Definition
X_train = [
    [18, 0, 0, 0, 0, 1, 1], # Safe: google.com
    [24, 0, 0, 0, 0, 2, 1], # Safe: github.com
    [42, 0, 0, 0, 1, 3, 1], # Phishing: secure-login.github.com
    [65, 0, 1, 0, 1, 4, 0], # Phishing: example.com@phish-site.com
    [15, 1, 0, 0, 0, 3, 0], # Phishing: 192.168.1.1/login
    [52, 0, 0, 1, 0, 2, 1], # Phishing: bit.ly/3xyz
    [22, 0, 0, 0, 0, 1, 1], # Safe: openai.com
    [75, 0, 0, 0, 1, 5, 0], # Phishing: update-account-bank-security-verify.com
    [29, 0, 0, 0, 0, 2, 1], # Safe: stackoverflow.com
    [60, 1, 0, 0, 1, 3, 0], # Phishing: 10.0.0.1/verify-banking
    [31, 0, 0, 0, 0, 2, 1], # Safe: wikipedia.org
    [68, 0, 1, 1, 1, 4, 0], # Phishing: t.co/xyz@secure-login
]
y_train = [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1]

# Step 3: Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Scan Function with Probability Score
def scan_url(url):
    if not url.strip():
        return "Please enter a valid URL."
    
    feats = [extract_advanced_features(url)]
    prediction = model.predict(feats)[0]
    probability = model.predict_proba(feats)[0]
    confidence = float(max(probability)) * 100
    
    if prediction == 1:
        return f"🚨 WARNING: High Phishing Risk Detected! ({confidence:.2f}% confidence)\nAnalysis: Suspicious heuristic patterns identified."
    else:
        return f"✅ SAFE: This URL appears legitimate. ({confidence:.2f}% confidence)"

# Step 5: Web UI Layout
with gr.Blocks(title="PhishGuard AI Advanced") as demo:
    gr.Markdown("# 🛡️ PhishGuard AI: Advanced Cybersecurity Threat Scanner")
    gr.Markdown("Real-time URL threat classification using heuristic feature extraction and a Random Forest classifier.")
    
    with gr.Row():
        url_input = gr.Textbox(label="Target URL", placeholder="Enter URL to analyze...")
    
    scan_btn = gr.Button("Analyze URL Security", variant="primary")
    result_output = gr.Textbox(label="Security Threat Analysis Report")
    
    scan_btn.click(fn=scan_url, inputs=url_input, outputs=result_output)

demo.launch(share=True)
