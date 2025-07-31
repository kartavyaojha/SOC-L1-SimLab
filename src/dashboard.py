import streamlit as st
import pandas as pd
import uuid
from datetime import datetime
import os

# File paths can be an issue if folder structure changes — consider using config or env variables later
ALERTS_FILE = '../data/alerts.csv'
TICKETS_FILE = '../data/tickets.csv'

# Streamlit caching here for the alerts, as alerts won't likely change often during session
@st.cache_data
def load_alerts():
    return pd.read_csv(ALERTS_FILE)

# Load existing tickets or create an empty DataFrame structure on first run
def load_tickets():
    if os.path.exists(TICKETS_FILE):
        return pd.read_csv(TICKETS_FILE)
    else:
        columns = ['ticket_id', 'alert_idx', 'timestamp', 'event_type',
                   'action', 'notes', 'status', 'time_handled']
        return pd.DataFrame(columns=columns)

# Appends the new ticket to CSV — this keeps it simple, no DB needed for this scale
def save_ticket(ticket):
    # Minor optimization: load tickets once & append, but watch for concurrency if multiple users
    df = load_tickets()
    df = df.append(ticket, ignore_index=True)
    df.to_csv(TICKETS_FILE, index=False)

# Severity colors help analysts scan alerts fast on criticality
SEVERITY_COLORS = {
    "Critical": "red",
    "High": "orange",
    "Medium": "goldenrod",
    "Low": "gray"
}

# Streamlit page config and title — keep wide since you use sidebar heavily
st.set_page_config(page_title="SOC-L1 Analyst SimLab", layout="wide")
st.title("🛡️ SOC-L1 Analyst SimLab")

# Load data
alerts = load_alerts()
tickets = load_tickets()

# Persistent state for keeping track of current alert index across reruns
if 'alert_idx' not in st.session_state:
    st.session_state.alert_idx = 0

# Sidebar: progress, reset, ticket log
with st.sidebar:
    st.header("Progress")
    st.markdown(f"**Alert:** {st.session_state.alert_idx + 1} / {len(alerts)}")

    # Reset makes trainer/dev life easier during testing or demos
    if st.button("🔄 Reset Session"):
        st.session_state.alert_idx = 0
        st.experimental_rerun()

    st.markdown("---")
    # 🏁 PERFORMANCE DASHBOARD ADDITION
    st.markdown('---')
    st.header("Performance Dashboard")

    if not tickets.empty:
        total_handled = len(tickets)
        actions = tickets['action'].value_counts().to_dict()
        avg_time = None
        if len(tickets) > 1:
            # For  later track individual alert open/close times,  
            # For now just time between first and last submit divided by tickets
            times = pd.to_datetime(tickets['time_handled'])
            elapsed = (times.max() - times.min()).total_seconds() / 60
            avg_time = elapsed / (len(times) - 1) if len(times) > 1 else 0

        st.metric("Alerts Handled", total_handled)
        st.metric("Escalated", actions.get('Escalate', 0))
        st.metric("Closed (FP)", actions.get('Close as False Positive', 0))
        st.metric("Info Requested", actions.get('Request More Info', 0))
        if avg_time is not None and avg_time > 0:
            st.metric("Avg Time / Ticket (min)", f"{avg_time:.2f}")
    else:
        st.info("Handle some alerts to see your performance ⏱️")

    st.header("Tickets Log")
    if tickets.empty:
        st.info("No tickets submitted yet.")
    else:
        # Limit tickets shown - in prod, add paging or filtering
        st.dataframe(
            tickets[['time_handled', 'event_type', 'action', 'status', 'notes']]
            .sort_values(by='time_handled', ascending=False)
            .reset_index(drop=True)
            .head(50)  # limit to most recent 50 for UI responsiveness
        )

# Main content: show alert or finish message
if st.session_state.alert_idx >= len(alerts):
    st.balloons()
    st.success("🎉 All alerts handled! Review your tickets in the sidebar.")
else:
    alert = alerts.iloc[st.session_state.alert_idx]
    severity_color = SEVERITY_COLORS.get(alert['severity'], 'black')

    # Clean alert header with progress
    st.markdown(f"### Alert {st.session_state.alert_idx + 1} of {len(alerts)}")
    cols = st.columns([2, 2, 2, 4])

    # Use metric for timestamp and IP, a colored label for severity, and detailed description
    cols[0].metric("⏰ Timestamp", alert['timestamp'])
    cols[1].metric("🌐 Source IP", alert['source_ip'])
    cols[2].markdown(
        f"<span style='color:{severity_color}; font-weight:bold;'>{alert['severity']}</span>",
        unsafe_allow_html=True
    )
    cols[3].markdown(f"**{alert['event_type']}** — {alert['description']}")

    st.markdown("---")

    # Analyst triage actions - radio horizontal for quick decision making
    action = st.radio("Action:", ['Escalate', 'Close as False Positive', 'Request More Info'], horizontal=True)
    notes = st.text_area("Analyst Notes (required):", height=120)

    # SOP guide - lightweight, expandable to avoid clutter while helping junior analysts
    with st.expander("Show SOP Guide & Analyst Tips"):
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
        tip = SOP.get(alert['event_type'], "Follow SOC runbook and escalate if unsure.")
        st.info(tip)

    # Submit button with validation
    if st.button("Submit Ticket 🚨"):
        if not notes.strip():
            st.warning("Analyst notes are required. Please provide your observations or rationale.")
        else:
            ticket = {
                'ticket_id': str(uuid.uuid4()),  # unique ticket id for traceability
                'alert_idx': st.session_state.alert_idx,
                'timestamp': alert['timestamp'],
                'event_type': alert['event_type'],
                'action': action,
                'notes': notes.strip(),
                'status': 'Open' if action == 'Escalate' else 'Closed',
                'time_handled': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
            }
            save_ticket(ticket)
            st.success(f"Ticket {ticket['ticket_id'][:8]} saved and logged.")
            st.session_state.alert_idx += 1  # advance to next alert
            st.experimental_rerun()  # rerun to refresh UI and load next alert
