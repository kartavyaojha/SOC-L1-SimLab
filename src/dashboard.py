import streamlit as st
import uuid
from datetime import datetime

from utils.data_utils import load_alerts, load_tickets, save_ticket, SEVERITY_COLORS, SOP

st.set_page_config(page_title="SOC-L1 Analyst SimLab", layout="wide")
st.title("🛡️ SOC-L1 Analyst SimLab")

# Load data
alerts = load_alerts()
tickets = load_tickets()

# Keep track of current alert index across reruns
if 'alert_idx' not in st.session_state:
    st.session_state.alert_idx = 0

# Sidebar UI
with st.sidebar:
    st.header("Progress")
    st.markdown(f"**Alert:** {st.session_state.alert_idx + 1} / {len(alerts)}")

    if st.button("🔄 Reset Session"):
        st.session_state.alert_idx = 0
        st.experimental_rerun()

    st.markdown("---")

    st.header("Tickets Log")
    if tickets.empty:
        st.info("No tickets submitted yet.")
    else:
        st.dataframe(
            tickets[['time_handled', 'event_type', 'action', 'status', 'notes']]
            .sort_values(by='time_handled', ascending=False)
            .reset_index(drop=True)
            .head(50)  # limit to recent 50 for UI speed
        )

# Main alert triage area
if st.session_state.alert_idx >= len(alerts):
    st.balloons()
    st.success("🎉 All alerts handled! Check your tickets in the sidebar.")
else:
    alert = alerts.iloc[st.session_state.alert_idx]
    severity_color = SEVERITY_COLORS.get(alert['severity'], 'black')

    st.markdown(f"### Alert {st.session_state.alert_idx + 1} of {len(alerts)}")
    cols = st.columns([2, 2, 2, 4])

    cols[0].metric("⏰ Timestamp", alert['timestamp'])
    cols[1].metric("🌐 Source IP", alert['source_ip'])
    cols[2].markdown(
        f"<span style='color:{severity_color}; font-weight:bold;'>{alert['severity']}</span>",
        unsafe_allow_html=True,
    )
    cols[3].markdown(f"**{alert['event_type']}** — {alert['description']}")

    st.markdown("---")

    # Analyst decision input
    action = st.radio("Action:", ['Escalate', 'Close as False Positive', 'Request More Info'], horizontal=True)
    notes = st.text_area("Analyst Notes (required):", height=120)

    # SOP guide
    with st.expander("Show SOP Guide & Analyst Tips"):
        tip = SOP.get(alert['event_type'], "Follow SOC runbook and escalate if unsure.")
        st.info(tip)

    if st.button("Submit Ticket 🚨"):
        if not notes.strip():
            st.warning("Please provide analyst notes before submitting the ticket.")
        else:
            ticket = {
                'ticket_id': str(uuid.uuid4()),
                'alert_idx': st.session_state.alert_idx,
                'timestamp': alert['timestamp'],
                'event_type': alert['event_type'],
                'action': action,
                'notes': notes.strip(),
                'status': 'Open' if action == 'Escalate' else 'Closed',
                'time_handled': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
            }
            save_ticket(ticket)
            st.success(f"Ticket {ticket['ticket_id'][:8]} saved.")
            st.session_state.alert_idx += 1
            st.experimental_rerun()
