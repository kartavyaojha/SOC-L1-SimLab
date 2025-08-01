import streamlit as st
from utils.data_utils import load_alerts, SEVERITY_COLORS

alerts = load_alerts()

if 'handled_alerts' not in st.session_state:
    st.session_state.handled_alerts = set()
if 'investigate_idx' not in st.session_state:
    st.session_state.investigate_idx = None

st.markdown("""
    <style>
    .alert-card {
        background: linear-gradient(90deg, #161822 97%, #2a2733 100%);
        border-left: 5px solid #ee4266;
        border-radius: 6px;
        box-shadow: 0 2px 15px #13141a77;
        padding: 1.15rem 1.1rem 1rem 1.4rem;
        margin-bottom: 1.35rem;
        color: #e0e8ef;
        font-family: 'JetBrains Mono', 'Fira Mono', monospace;
        position: relative;
        overflow: hidden;
    }
    .severity-badge {
        display: inline-block;
        padding: 0.12rem 0.82rem 0.12rem 0.82rem;
        border-radius: 4px;
        font-weight: 900;
        font-size: 1.06em;
        letter-spacing: 0.04em;
        margin-bottom: 5px;
        margin-right: 11px;
        background: #1a1d29;
        color: #ee4266;
        border-left: 4px solid #ee4266;
        box-shadow: inset 0 0 7px #ee4266;
    }
    .severity-high    { color: #fd9300; border-left:4px solid #fd9300 !important; box-shadow:inset 0 0 6px #fd9300;}
    .severity-medium  { color: #ffc23c; border-left:4px solid #ffc23c !important; box-shadow:inset 0 0 4px #ffc23c;}
    .severity-low     { color: #68b2fa; border-left:4px solid #68b2fa !important; box-shadow:inset 0 0 5px #68b2fa;}
    .alert-card hr {border: 0; height:1px; background:#232332;margin:9px 0 14px 0;}
    .alert-card .meta { color:#a6b0ce;font-size:0.96em; }
    .btn-urgent {
        font-weight: 900;
        color: #fff;
        background: linear-gradient(90deg,#ee4266 72%,#fd9300 100%);
        border: 0;
        box-shadow: 0 0 6px #ee4266a0;
        border-radius: 3px;
        margin-top: 12px;
        width: 100%;
        padding: 0.5em;
        font-size: 1.05em;
        transition:0.17s opacity;
    }
    .btn-urgent:hover { opacity: 0.91; }
    </style>
""", unsafe_allow_html=True)

st.title("🔻 ACTIVE INCIDENTS | SOC-1 War Room")

alert_indices = [idx for idx in range(len(alerts)) if idx not in st.session_state.handled_alerts]

if not alert_indices:
    st.success("🎉 All incidents triaged. No active alerts remain.")
else:
    cols = st.columns(2)
    for i, idx in enumerate(alert_indices):
        alert = alerts.iloc[idx]
        sev = alert['severity']
        badge_class = "severity-badge"
        if sev == "High":
            badge_class += " severity-high"
        elif sev == "Medium":
            badge_class += " severity-medium"
        elif sev == "Low":
            badge_class += " severity-low"

        with cols[i % 2]:
            st.markdown(
                f"""<div class="alert-card">
                    <span class="{badge_class}">{sev}</span>
                    <span style="float:right;color:#aaa9b7;font-size:1em;">
                        {alert['timestamp']}
                    </span>
                    <br>
                    <strong>Incident:</strong> <span style='color:#68b2fa'>{alert['event_type']}</span>
                    <br>
                    <span class='meta'>{alert['description']}</span>
                    <hr>
                    <span class="meta"><b>Source:</b> {alert['source_ip']} &nbsp;&bull;&nbsp;{
                        "<b>Dest:</b> "+str(alert.get('destination_ip',"")) if alert.get('destination_ip') else ""
                    }{
                        "&nbsp;&bull;&nbsp;<b>Asset:</b> "+str(alert.get('asset',"")) if alert.get('asset') else ""
                    }</span>
                """, unsafe_allow_html=True
            )
            with st.expander("Show More Details"):
                detail_fields = {
                    "Username": alert.get("username", ""),
                    "Location": alert.get("location", ""),
                    "Detection Tool": alert.get("detection_tool", "")
                }
                for label, value in detail_fields.items():
                    if value:
                        st.write(f"**{label}:** {value}")
                if alert.get("raw_log"):
                    st.markdown("**Raw Log/Event:**")
                    st.code(str(alert.get("raw_log")), language="text")

            if st.button(
                f"Investigate Incident • {sev.upper()}",
                key=f"investigate_{idx}",
                help="Go to investigation portal for this incident"
            ):
                st.session_state.investigate_idx = idx
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
