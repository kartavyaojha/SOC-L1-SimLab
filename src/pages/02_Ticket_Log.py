import streamlit as st
from utils.data_utils import load_tickets

st.title("📝 Ticket Log")

tickets = load_tickets()

if tickets.empty:
    st.info("No tickets submitted yet.")
else:
    tickets_display = tickets.copy()
    tickets_display['Result'] = tickets_display['correct'].map(lambda x: "✅" if x else "❌")

    display_cols = [
        'time_handled', 'event_type', 'action', 'status', 'notes', 'Result',
        'source_ip', 'destination_ip', 'username', 'asset', 'location', 'detection_tool'
    ]

    st.dataframe(
        tickets_display[display_cols]
            .sort_values(by='time_handled', ascending=False)
            .reset_index(drop=True)
            .head(100)
    )
