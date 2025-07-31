import pandas as pd
import os
import streamlit as st

# Configurable file paths with environment variable fallback
ALERTS_FILE = os.getenv('ALERTS_FILE_PATH', '../data/alerts.csv')
TICKETS_FILE = os.getenv('TICKETS_FILE_PATH', '../data/tickets.csv')

# Severity colors for quick UI highlighting
SEVERITY_COLORS = {
    "Critical": "red",
    "High": "orange",
    "Medium": "goldenrod",
    "Low": "gray"
}

# SOP tips keyed by event type
SOP = {
    'Brute-force': "Check failed login patterns, user account status, consider lockout policies.",
    'Port Scan': "Map scanning IP, escalate if frequent or combined with other suspicious events.",
    'Malware Detected': "Immediately escalate and isolate affected hosts. Initiate full malware scan.",
    'Suspicious Login': "Verify user location, device. Notify user. Escalate if unauthorized.",
    'Phishing Email': "Block sender/domain, report to SOC team, warn end-user.",
    'Data Exfiltration Attempt': "Critical! Escalate and begin incident response immediately.",
    'Privilege Escalation': "Check process tree, escalate to IR team.",
    'Ransomware Activity': "Critical - isolate system, notify incident response immediately.",
    'Suspicious DNS Query': "Check IP/domain reputation, escalate if malicious.",
    'Unauthorized Access': "Alert user and security team promptly.",
    'Web Shell Detected': "Immediate escalation to incident response required.",
    'Malicious Script Execution': "Validate source; escalate if illicit.",
    'Failed MFA Attempt': "Repeated failures should trigger escalation.",
    'Suspicious Process': "Investigate process origin, escalate if needed.",
    'Exploit Attempt': "Critical — patch and escalate urgently.",
}

@st.cache_data
def load_alerts(file_path=ALERTS_FILE):
    try:
        df = pd.read_csv(file_path)
        required_columns = {'timestamp', 'source_ip', 'event_type', 'severity', 'description'}
        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError(f'Alerts CSV missing required columns: {missing}')
        return df
    except FileNotFoundError:
        st.error(f"Alerts file not found at path: {file_path}")
        st.stop()
    except Exception as e:
        st.error(f"Error loading alerts CSV: {e}")
        st.stop()

def load_tickets(file_path=TICKETS_FILE):
    try:
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            return df
        else:
            columns = ['ticket_id', 'alert_idx', 'timestamp', 'event_type', 'action', 'notes', 'status', 'time_handled']
            return pd.DataFrame(columns=columns)
    except Exception as e:
        st.error(f"Error loading tickets CSV: {e}")
        st.stop()

def save_ticket(ticket: dict, file_path=TICKETS_FILE):
    try:
        df = load_tickets(file_path)
        new_df = pd.DataFrame([ticket])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(file_path, index=False)
    except Exception as e:
        st.error(f"Error saving ticket: {e}")
