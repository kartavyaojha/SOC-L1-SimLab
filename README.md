SOC-L1 SimLab

    Simulate real-world L1 SOC alert triage, ticketing, and response. Build your analyst instincts with practical hands-on workflows.

🚀 Quick Start

    Clone & Install:

bash
git clone https://github.com/yourusername/SOC-L1-SimLab.git
cd SOC-L1-SimLab
pip install -r requirements.txt

Run the App:

    bash
    streamlit run src/dashboard.py

    Customize Alerts:
    Edit or add alerts in data/alerts.csv (format provided below).

✨ Features

    One-by-one alert triage: Feels like a real SOC queue—handle what pops in, not a giant list dump.

    Actions: Escalate, close as false positive, or request more info—each action opens a ticket with your notes.

    Ticket log: Every action documented. Go back and review what you did.

    Built-in SOP cheat sheet: Get context/recommendations for each alert or action (think “runbook quick reference”).

    Easy to extend: Data in CSV, Python code is modular—modify or add your own alert types/features.

Up Next / Ideas:

    Gamification (“Nice triage!” or “Hmm, check best practice”)

    Hotkeys for faster analyst flow.

    Analyst stats dashboard (response time, accuracy, etc.)

💻 Data/Architecture Diagram

text
[alerts.csv]     +------------------------+
     |   ---->   |   Streamlit Dashboard  |
     |           +------------------------+
     |                  | |  |   |
     |                  | |  |   +------> [SOP Guide]     # In-line help/docs
     |                  | |  +---------> [Triage Panel]   # Alert decisions
     |                  | +------------> [Ticketing]      # Log actions/notes
     +---------------------------------> [tickets.csv]     # Persisted logs

📄 Sample alerts.csv

text
timestamp,source_ip,event_type,severity,description
2025-07-31 10:20,192.168.1.10,Brute-force,Medium,Multiple failed SSH logins
2025-07-31 10:22,10.10.10.22,Malware,High,Ransomware flagged on endpoint
2025-07-31 10:26,172.16.0.5,Phishing,High,Suspicious email with dangerous attachment

🛠 Why This Design?

    Looks and feels like a real L1 SOC desk: Fast triage, simple documentation, immediate feedback.

    CSV for customization: Swap in your own scenarios, use in demos, or extend with minimal setup.

    No fluff—just skills: Focus on decisions, learning, and documentation. The stuff that makes good analysts great.

👋 Contributing / License

PRs welcome! Built for learning, training, and interviews. MIT License.
