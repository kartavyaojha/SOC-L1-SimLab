import streamlit as st
import uuid
from datetime import datetime
from utils.data_utils import load_alerts, save_ticket, get_correct_actions_for_alert, SOP

alerts = load_alerts()

idx = st.session_state.get('investigate_idx', None)

if idx is None or idx >= len(alerts):
    st.warning("No alert selected for investigation. Please select an alert from the main channel.")
    if st.button("Go to Main Channel"):
        st.session_state.investigate_idx = None
        st.rerun()

else:
    alert = alerts.iloc[idx]
    st.title("🕵️ Investigation Portal")
    st.markdown(f"### Alert Details: {alert['event_type']} ({alert['severity']})")
    st.markdown(f"**Timestamp:** {alert['timestamp']}")
    st.markdown(f"**Source IP:** {alert['source_ip']}")
    st.markdown(f"**Destination IP:** {alert.get('destination_ip', 'N/A')}")
    st.markdown(f"**Username:** {alert.get('username', 'N/A')}")
    st.markdown(f"**Asset:** {alert.get('asset', 'N/A')}")
    st.markdown(f"**Location:** {alert.get('location', 'N/A')}")
    st.markdown(f"**Detection Tool:** {alert.get('detection_tool', 'N/A')}")
    st.markdown(f"**Description:** {alert['description']}")
    if alert.get("raw_log"):
        st.markdown("**Raw Log/Event:**")
        st.code(str(alert.get("raw_log")), language="text")

    with st.expander("SOP Guide & Analyst Tips"):
        tip = SOP.get(alert['event_type'], "Follow SOC runbook and escalate if unsure.")
        st.info(tip)

    action = st.radio("Select your action:", ['Escalate', 'Close as False Positive', 'Request More Info'], horizontal=True)
    notes = st.text_area("Analyst Notes (required):", height=120)

    if st.button("Submit Investigation"):
        if not notes.strip():
            st.warning("Please provide analyst notes before submitting the investigation.")
        else:
            correct_actions = get_correct_actions_for_alert(alert)
            is_correct = action in correct_actions

            ticket = {
                'ticket_id': str(uuid.uuid4()),
                'alert_idx': idx,
                'timestamp': alert['timestamp'],
                'event_type': alert['event_type'],
                'action': action,
                'notes': notes.strip(),
                'status': 'Open' if action == 'Escalate' else 'Closed',
                'time_handled': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
                'correct': is_correct,
                'source_ip': alert.get('source_ip', ''),
                'destination_ip': alert.get('destination_ip', ''),
                'username': alert.get('username', ''),
                'asset': alert.get('asset', ''),
                'location': alert.get('location', ''),
                'detection_tool': alert.get('detection_tool', ''),
                'raw_log': alert.get('raw_log', '')
            }
            save_ticket(ticket)

            if 'handled_alerts' not in st.session_state:
                st.session_state.handled_alerts = set()
            st.session_state.handled_alerts.add(idx)
            st.session_state.investigate_idx = None

            if is_correct:
                st.success("✅ Ticket saved. Your triage decision is correct!")
            else:
                st.warning(f"❌ Ticket saved, but your triage decision may be incorrect. Recommended: {', '.join(correct_actions)}")

            if st.button("Return to Main Channel"):
                st.rerun()
