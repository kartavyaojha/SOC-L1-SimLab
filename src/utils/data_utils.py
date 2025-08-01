import pandas as pd
import os
import streamlit as st
from pathlib import Path

# File path setup
UTILS_DIR = Path(__file__).parent
PROJECT_ROOT = UTILS_DIR.parent.parent

ALERTS_FILE = os.getenv('ALERTS_FILE_PATH', str(PROJECT_ROOT / 'data' / 'alerts.csv'))
TICKETS_FILE = os.getenv('TICKETS_FILE_PATH', str(PROJECT_ROOT / 'data' / 'tickets.csv'))

# Severity color mapping for UI
SEVERITY_COLORS = {
    "Critical": "red",
    "High": "orange",
    "Medium": "goldenrod",
    "Low": "gray"
}

# Standard Operating Procedures tips
SOP = {
    'Brute-force': "Look for repeated failed auth attempts in short time windows.",
    'Port Scan': "Check if scan originated by known IT maintenance or suspicious source.",
    'Malware Detected': "Escalate immediately for infection containment and cleanup.",
    'Suspicious Login': "Verify location, travel info, and notify user to confirm legitimacy.",
    'Phishing Email': "Block sender, report threat, and educate user to avoid re-occurrence.",
    'Data Exfiltration Attempt': "Critical — isolate host immediately and escalate SOC/IR.",
    'Privilege Escalation': "Investigate process chains; often precursor to lateral movement.",
    'Ransomware Activity': "Isolate endpoints and escalate to incident response team urgently.",
    'Suspicious DNS Query': "Check domain reputation; suspicious traffic could indicate C2.",
    'Unauthorized Access': "Verify credentials and lock accounts if compromise suspected.",
    'Web Shell Detected': "Immediate remediation needed; check webserver integrity.",
    'Malicious Script Execution': "Contain and investigate source user/process.",
    'Failed MFA Attempt': "Repeated failures could indicate MFA brute-force; escalate as necessary.",
    'Suspicious Process': "Analyze behavior for binary reputation and context.",
    'Exploit Attempt': "Patch vulnerable systems immedately and escalate.",
}

# Mapping event_type to correct triage actions
CORRECT_ACTIONS = {
    'Phishing Email': ['Escalate', 'Request More Info'],
    'Malware Detected': ['Escalate'],
    'Brute-force': ['Escalate', 'Request More Info'],
    'Port Scan': ['Escalate', 'Request More Info'],
    'Data Exfiltration Attempt': ['Escalate'],
    'Ransomware Activity': ['Escalate'],
    'Unauthorized Access': ['Escalate'],
    'Suspicious Login': ['Escalate', 'Request More Info'],
    'Suspicious DNS Query': ['Escalate', 'Request More Info'],
    'Web Shell Detected': ['Escalate'],
    'Malicious Script Execution': ['Escalate'],
    'Failed MFA Attempt': ['Escalate'],
    'Suspicious Process': ['Escalate', 'Request More Info'],
    'Exploit Attempt': ['Escalate'],
    'Privilege Escalation': ['Escalate'],
    # False positives expect 'Close as False Positive' — handled below.
}

@st.cache_data
def load_alerts(file_path=ALERTS_FILE):
    try:
        df = pd.read_csv(file_path)
        required_cols = {'timestamp', 'source_ip', 'event_type', 'severity', 'description'}
        missing_cols = required_cols - set(df.columns)
        if missing_cols:
            raise ValueError(f"Alerts CSV missing columns: {missing_cols}")

        # Ensure the false positive column exists and is boolean
        if 'is_false_positive' not in df.columns:
            df['is_false_positive'] = False
        else:
            df['is_false_positive'] = df['is_false_positive'].astype(bool)

        # Fill any additional optional columns if missing
        for col in ['destination_ip', 'username', 'asset', 'location', 'detection_tool', 'raw_log']:
            if col not in df.columns:
                df[col] = ''

        return df
    except FileNotFoundError:
        st.error(f"Alerts file not found at path: {file_path}")
        st.stop()
    except Exception as e:
        st.error(f"Error reading alerts CSV: {e}")
        st.stop()

def get_correct_actions_for_alert(alert):
    if alert.get('is_false_positive', False):
        return ['Close as False Positive']
    return CORRECT_ACTIONS.get(alert['event_type'], ['Escalate'])

def load_tickets(file_path=TICKETS_FILE):
    base_columns = [
        'ticket_id', 'alert_idx', 'timestamp', 'event_type', 'action', 'notes',
        'status', 'time_handled', 'correct',
        'source_ip', 'destination_ip', 'username', 'asset', 'location',
        'detection_tool', 'raw_log'
    ]
    try:
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            # Add missing columns for backward compatibility
            for col in base_columns:
                if col not in df.columns:
                    df[col] = ''
            return df[base_columns]
        else:
            return pd.DataFrame(columns=base_columns)
    except Exception as e:
        st.error(f"Error reading tickets CSV: {e}")
        st.stop()

def save_ticket(ticket: dict, file_path=TICKETS_FILE):
    try:
        df = load_tickets(file_path)
        new_df = pd.DataFrame([ticket])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(file_path, index=False)
    except Exception as e:
        st.error(f"Error saving ticket: {e}")
