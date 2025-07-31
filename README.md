# **SOC-L1 SimLab**

> **Simulate real-world L1 SOC alert triage, ticketing, and response. Build your analyst instincts with practical hands-on workflows.**

## **🚀 Quick Start**

1. **Clone & Install:**
    ```
    git clone https://github.com/yourusername/SOC-L1-SimLab.git
    cd SOC-L1-SimLab
    pip install -r requirements.txt
    ```

2. **Run the App:**
    ```
    streamlit run src/dashboard.py
    ```

3. **Customize Alerts:**  
   Edit or add alerts in `data/alerts.csv` (format provided below).

## **✨ Features**

- **One-by-one alert triage:** Feels like a real SOC queue—handle what pops in, not a giant list dump.
- **Actions:** Escalate, close as false positive, or request more info—each action opens a ticket with your notes.
- **Ticket log:** Every action documented. Go back and review what you did.
- **Built-in SOP cheat sheet:** Get context/recommendations for each alert or action (think “runbook quick reference”).
- **Easy to extend:** Data in CSV, Python code is modular—modify or add your own alert types/features.

**Up Next / Ideas:**
- Gamification (“Nice triage!” or “Hmm, check best practice”)
- Hotkeys for faster analyst flow.
- Analyst stats dashboard (response time, accuracy, etc.)

## **💻 Data/Architecture Diagram**
# **SOC-L1 SimLab**

> **Simulate real-world L1 SOC alert triage, ticketing, and response. Build your analyst instincts with practical hands-on workflows.**

## **🚀 Quick Start**

1. **Clone & Install:**
    ```
    git clone https://github.com/yourusername/SOC-L1-SimLab.git
    cd SOC-L1-SimLab
    pip install -r requirements.txt
    ```

2. **Run the App:**
    ```
    streamlit run src/dashboard.py
    ```

3. **Customize Alerts:**  
   Edit or add alerts in `data/alerts.csv` (format provided below).

## **✨ Features**

- **One-by-one alert triage:** Feels like a real SOC queue—handle what pops in, not a giant list dump.
- **Actions:** Escalate, close as false positive, or request more info—each action opens a ticket with your notes.
- **Ticket log:** Every action documented. Go back and review what you did.
- **Built-in SOP cheat sheet:** Get context/recommendations for each alert or action (think “runbook quick reference”).
- **Easy to extend:** Data in CSV, Python code is modular—modify or add your own alert types/features.

**Up Next / Ideas:**
- Gamification (“Nice triage!” or “Hmm, check best practice”)
- Hotkeys for faster analyst flow.
- Analyst stats dashboard (response time, accuracy, etc.)

## 🗺️ Architecture Diagram

![SOC-L1 SimLab Architecture](assets/architecture-diagram.png)


## **📄 Sample alerts.csv**
- timestamp,source_ip,event_type,severity,description
```
 2025-07-31 10:20,192.168.1.10,Brute-force,Medium,Multiple failed SSH logins
 2025-07-31 10:22,10.10.10.22,Malware,High,Ransomware flagged on endpoint
 2025-07-31 10:26,172.16.0.5,Phishing,High,Suspicious email with dangerous attachment
```
- For more advanced SOC scenarios, just swap the sample with the full assets/alerts.csv file. Contributions for even more alert types are welcome!




















![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%94-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


