import streamlit as st
from utils.data_utils import load_alerts, load_tickets

alerts = load_alerts()
tickets = load_tickets()

if 'handled_alerts' not in st.session_state:
    st.session_state.handled_alerts = set()

st.title("📊 Progress Dashboard")

total_alerts = len(alerts)
triaged_count = len(st.session_state.handled_alerts)
st.markdown(f"### Alerts Progress: {triaged_count} of {total_alerts} triaged")

progress_pct = triaged_count / total_alerts if total_alerts else 0.0
st.progress(progress_pct)

total_tickets = len(tickets)
correct_tickets = tickets['correct'].sum() if not tickets.empty else 0
accuracy = (correct_tickets / total_tickets * 100) if total_tickets > 0 else 0

st.write(f"Total tickets submitted: {total_tickets}")
st.write(f"Correct triages: {correct_tickets} ({accuracy:.1f}%)")

if st.button("Reset Progress"):
    st.session_state.handled_alerts = set()
    st.rerun()
