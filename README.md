# SOC-L1 SimLab — Next-Gen Blue Team Triage Platform

> _From learners, for learners. Simulate true-to-life Security Operations alert investigation, documentation, and decision-making in a modern, immersive environment._

## 🚀 Quick Start
    
    git clone https://github.com/kartavyaojha/SOC-L1-SimLab.git
    cd SOC-L1-SimLab
    pip install -r requirements.txt
    python -m streamlit run .\src\dashboard.py
    

## 🖥️ What Is It?

A serious, hands-on platform to:
- **Practice real SOC L1 investigative skills:** Each incident is a unique card, not a gamified pop quiz.
- **Experience uncertainty:** You’ll see ambiguous, real-world events—no answer is obvious.
- **Act like a true analyst:** Triage, dive deep, research context, log decisions with notes.

## ✨ Features

- **🔻 Modern "War Room" Dashboard:** See all active incidents in an intense, card-based grid—severity color-coded, hacker-terminal fonts, and dark cyberpunk/CTF-inspired style.
- **🌗 Deep Investigation Workflow:** Every alert leads to its own investigation portal—an environment for decisive action and real research.
- **📚 Authentic Details:** Each event includes contextual fields (_IPs, users, asset, logs, detection source, etc._), not just trivial clues—and never leaks the answer.
- **✅ Ticketing & Feedback:** All analyst actions are logged, with instant accuracy feedback (after, never before).
- **📈 Progress Tracking:** Dedicated dashboard: see triaged, accuracy stats, and push your analyst instincts further.
- **📋 Clean Ticket Log:** Review your decisions and learning from prior cases.
- **👾 “About the Maker” & Terminal Bio:** Professional, cyberpunk, and terminal-style about pages showcase the project origins, for the community, by the community.

## 📁 Folder Structure
    SOC-L1-SimLab/
    ├── data/
    │ ├── alerts.csv # All active/archived incident data
    │ └── tickets.csv # Your triage history (auto-generated)
    ├── src/
    │ ├── dashboard.py # Main alert dashboard, updated war room UI
    │ ├── utils/
    │ │ └── data_utils.py
    │ └── pages/
    │ ├── 01_Progress.py
    │ ├── 02_Ticket_Log.py
    │ ├── 03_Investigation.py
    │ ├── 04_About.py
    │ └── 05_Terminal_About.py


## 🗃️ How It Works

1. **Alerts:** Each incident is a card—explore summary & more details; nothing is obvious, just like a real SOC.
2. **Investigate:** Click "Investigate" to access a focused triage portal. Read, research, decide, and document.
3. **Action:** Choose: Escalate, Close as FP, or Request More Info. You must justify your reasoning.
4. **Record:** Decisions go to your ticket log, with rigorous feedback—so you learn, fast.
5. **Progress:** See summary stats, re-review cases, and always know which incidents remain.

## 🧑💻 For Learners, By a Learner

> “From brute-forcing the basics to building blue team platforms—this is for all digital explorers who believe you learn by doing. No flashy badges, no spoilers—just pure analyst growth.”

- **Builder:** [kartavyaojha](https://github.com/kartavyaojha)  
- **Contact:** kartavya9977@gmail.com  
- **Connect:** [LinkedIn](https://www.linkedin.com/in/kartavya-ojha)  
- _“Never stop poking, breaking, or building—the frontline welcomes all.”_

## 📄 Custom Alerts

_Edit or extend `data/alerts.csv` for new scenarios. Columns:_
timestamp,source_ip,destination_ip,username,event_type,severity,description,is_false_positive,asset,location,detection_tool,raw_log

Check the included CSV examples for full structure and realism.

## 🛡️ Why This Design?

- **No shortcuts. No spoilers.** Events are ambiguous—investigation required, not just guessing.
- **UI built for focus:** The war room grid, investigation pages, and logs support real analyst workflow.
- **Open source, modern, and ready for the next wave of blue teamers.**

## ⚡ Want to Contribute or Chat?

Pull requests, new alert data, workflow ideas, and CTF-style challenge contributions are all welcome!  
_This is your space to make analyst training more real and rewarding for all._

## 📜 License

MIT License — always free, for learning and for learners.

---

**Welcome to the field. Triage is open.**

---
![GitHub repo size](https://img.shields.io/github/repo-size/kartavyaojha/SOC-L1-SimLab?color=brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Issues](https://img.shields.io/github/issues/kartavyaojha/SOC-L1-SimLab?color=blue)

