# import streamlit as st

# # --- Custom CSS for the cyberpunk effect ---
# st.markdown("""
# <style>
# body, .stApp {
#     background: linear-gradient(135deg, #0e164c 0%, #141327 100%), #101018;
#     color: #33ff86;
#     font-family: 'Fira Code', 'VT323', 'JetBrains Mono', monospace !important;
#     min-height: 100vh;
#     position: relative;
#     overflow-x: hidden;
# }
# .cyber-avatar-frame {
#     border: 3.5px solid #33ffe6;
#     box-shadow: 0 0 16px 3px #6000ffbb, 0 0 30px #39ff14b0;
#     border-radius: 18px;
#     padding: 7px;
#     width: 155px;
#     background: rgba(24,21,52,0.8);
#     margin-right: 28px;
#     float: left;
#     margin-bottom: 8px;
#     position: relative;
#     outline: 2.3px dashed #39ff14;
#     outline-offset: 7px;
# }
# .cyber-bio-block {
#     background: rgba(20,18,56,0.88);
#     border-radius: 14px;
#     box-shadow: 0 2px 26px #230048e0;
#     padding: 1.5em 2.1em 1.7em 1.5em;
#     color: #b5fff1;
#     font-family: 'Fira Code', 'VT323', 'JetBrains Mono', monospace !important;
#     font-size: 1.1em;
#     margin-top: 8px;
# }
# .cyber-link {
#     color: #1cc3ff !important;
#     text-shadow: 0 0 9px #3a92fbc5, 0 0 2px #080233;
#     text-decoration: none;
#     transition: 0.18s color, 0.12s text-shadow;
#     font-weight: bold;
#     letter-spacing: 0.025em;
# }
# .cyber-link:hover {
#     color: #39ff14 !important;
#     text-shadow: 0 0 18px #39ff1482, 0 0 2px #0e003a;
#     animation: neon-flicker 0.22s infinite alternate;
# }
# @keyframes neon-flicker {
#   0% { opacity: 1; }
#   40% { opacity: .65; }
#   60% { opacity: 1; }
#   100% { opacity: .86; }
# }
# /* Digital noise effect */
# body:before, .css-18e3th9:before {
#     content:"";
#     pointer-events:none;
#     position:fixed;
#     width:100vw;
#     height:100vh;
#     left:0;top:0;
#     opacity: .055;
#     z-index:0;
#     background: url('https://upload.wikimedia.org/wikipedia/commons/9/9e/Noise_background.png');
#     mix-blend-mode: overlay;
# }
# /* Title effect */
# .cyberpunk-title {
#     font-family: 'Fira Code', 'JetBrains Mono', monospace;
#     font-size: 2.35em;
#     letter-spacing: 0.05em;
#     color: #33ff86;
#     text-shadow:
#       0 0 5px #5104c6,
#       0 0 12px #1cc3ff99,
#       0 0 20px #3a92fb66,
#       0 0 40px #39ff14bb;
#     margin-bottom:10px;
# }
# </style>
# """, unsafe_allow_html=True)

# # --- Page title with cyberpunk style ---
# st.markdown('<div class="cyberpunk-title">👾 About the Maker</div>', unsafe_allow_html=True)

# # --- Graffiti/hacker avatar with neon frame ---
# st.markdown(
#     """
#     <div class="cyber-avatar-frame">
#         <img src="https://avatars.githubusercontent.com/u/51846490?v=4" style="max-width:100%;border-radius:13px;display:block;">
#         <div style="color:#fd9300;font-family:'VT323',monospace;font-size:1.1em;text-align:center;margin-top:7px;letter-spacing:0.09em;text-shadow:0 0 8px #fd9300c0">kartavyaojha</div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # --- Main bio block ---
# st.markdown(
#     """
#     <div class="cyber-bio-block">
#         <span style="font-size:1.14em;font-family:'Fira Code','VT323',monospace;">
#         Hey! I’m Kartavya Ojha—a security enthusiast, Python wrangler, and proud member of the global SOC learner tribe.<br><br>
#         From brute-forcing my way through basics to building blue team projects and open-sourcing every “aha!” moment, I believe that in cybersecurity, we’re <b>all learners first—always</b>. The hunt, the hustle, the head-scratching bugs, and the big “got it!” breakthroughs keep this journey endlessly exciting.<br><br>
#         Whether you’re decoding your first SIEM alert, scripting your first firewall, or breaking and fixing things simply to learn, you’re already a part of the crew.<br><br>
#         This SOC-L1 SimLab project is for us: analysts, students, and explorers who know that <i>doing</i> is always the best way to grow.
#         </span>
#         <br><br>
#         <b>🧑‍💻 GitHub:</b> <a href="https://github.com/kartavyaojha" class="cyber-link" target="_blank">kartavyaojha</a> &nbsp;|&nbsp;
#         <b>🔗 LinkedIn:</b> <a href="https://www.linkedin.com/in/kartavya-ojha" class="cyber-link" target="_blank">kartavya-ojha</a><br>
#         <b>✉️ Say hi:</b> <a href="mailto:kartavya9977@gmail.com" class="cyber-link">kartavya9977@gmail.com</a>
#         <br><br>
#         <span style="color:#1cc3ff;text-shadow:0 0 7px #39ff14aa;">From one learner to another: never stop poking, breaking, or building. The frontline is open to anyone with curiosity and persistence.</span>
#         <br><br>
#         <span style="color:#a464fc;font-size:1.02em;">Let’s keep exploring—together.</span>
#     </div>
#     """,
#     unsafe_allow_html=True
# )


import streamlit as st

# --------- Terminal Hacker CSS ---------
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(160deg, #0e0e0e 0%, #22282d 100%) !important;
    color: #89ff7b !important;
    font-family: 'Fira Code', 'Courier New', 'JetBrains Mono', monospace !important;
    min-height: 100vh;
    box-sizing: border-box;
    letter-spacing: 0.01em;
}
.terminal-section-title {
    color: #bbff9d;
    border-left: 3.6px solid #39ff14;
    background: rgba(30,40,35,0.17);
    font-size: 1.16em;
    letter-spacing: 0.07em;
    margin-bottom: 7px;
    font-family: 'Fira Code', monospace;
    padding: 4px 0 4px 13px;
    margin-top: 21px;
    text-transform: uppercase;
}
.avatar-scanline {
    display: block;
    margin-bottom: 12px;
    margin-right: auto;
    margin-left: auto;
    max-width: 130px;
    filter: grayscale(27%) brightness(0.92) drop-shadow(0 0 9px #31c911dd);
    box-shadow: 0 0 36px #39ff1472;
    position:relative;
}
.avatar-scanline:after {
    content: "";
    display: block;
    position: absolute;
    left:0;top:0;
    width:100%;height:100%;
    pointer-events: none;
    background: repeating-linear-gradient(to bottom,rgba(57,255,20,0.12),rgba(57,255,20,0.16) 1.5px,transparent 2.5px, transparent 7px);
    z-index:1;
}
.term-block {
    background: rgba(7,9,12,0.92);
    border-radius: 9px;
    box-shadow: 0 0 22px #032214c7;
    padding: 1.4em 1.7em 1.6em 1.2em;
    color: #adffad;
    font-family: 'Fira Code','JetBrains Mono',monospace;
    font-size: 1.07em;
    margin-top: 5px;
}
.glitch-effect {
    color: #52fc43;
    font-family: 'Fira Code',monospace;
    display:inline-block;
    animation: hackerglitch 1.4s linear infinite alternate;
    font-size:1.19em;
    margin-left:4px;
    letter-spacing:0.05em;
}
@keyframes hackerglitch {
  0% { text-shadow: 0 0 1.8px #fff, 0 0 0 #3ae884; }
  18% { text-shadow: 2px 0 2.8px #39ff14, -0.7px 1px 1.4px #fff7; }
  33% { opacity: 0.81;}
  40% { text-shadow: 0 0 1.8px #fff, -2.1px 1.9px 1.7px #2dff10; opacity: 0.97;}
  55% { text-shadow: 0 0 9px #31a91455, 0 0 3.7px #fff; opacity: 0.77;}
  76% { text-shadow: 0 0 1.8px #fff;}
  100% { opacity: 1;}
}
.term-link {
    color: #72ffb4!important;
    font-family: 'Fira Code',monospace;
    border-bottom: 1.3px dotted #3ae88455;
    text-decoration:none;
    padding: 0 2px;
    transition: color 0.15s, border-bottom 0.13s;
}
.term-link:hover {
    color: #fff !important;
    border-bottom: 1.5px solid #1dbb17;
    text-shadow: 0 0 15px #31c911bb, 0 0 2px #fff;
}
.terminal-cursor {
    display:inline-block;
    background:#41ff361d;
    color: #41ff36;
    width:11px; height:1.3em;
    border-radius:2px;
    margin-left:1px;
    animation: blinkcursor 1.09s steps(1,end) infinite;
    vertical-align:bottom;
}
@keyframes blinkcursor {
  from, to { opacity: 0.19;}
  50% { opacity: 1;}
}
@media screen and (max-width: 700px) {
    .term-block {font-size: 0.96em;padding:1em 0.7em 1.3em 0.6em;}
    .terminal-section-title {font-size:0.98em;}
    .avatar-scanline {max-width:90px;}
}
</style>
""", unsafe_allow_html=True)


# st.markdown(
#     """
#     <div style="width:100%;text-align:center;">
#         <img src="src/avtar.png" alt="Graffiti hacker avatar" class="avatar-scanline">
#     </div>
#     """, unsafe_allow_html=True
# )


st.markdown('<div class="terminal-section-title">[NAME]</div>', unsafe_allow_html=True)
st.markdown('''
<div class="term-block">
  Kartavya Ojha<span class="terminal-cursor"></span>
</div>
''', unsafe_allow_html=True)

st.markdown('<div class="terminal-section-title">[SHORT BIO]</div>', unsafe_allow_html=True)
st.markdown('''
<div class="term-block">
  <span class="glitch-effect">from learner to learner</span><br>
  Security addict, code fiend, digital explorer. I thrive on breaking things so I can learn to fix them. This platform: built for everyone who thinks like a real blue teamer—not just a button pusher.<br>
  <i>"There are no masters, only persistent hackers."</i>
</div>
''', unsafe_allow_html=True)

st.markdown('<div class="terminal-section-title">[SKILLS]</div>', unsafe_allow_html=True)
st.markdown('''
<div class="term-block">
- Threat-hunting, SIEM, Python, Automation<br>
- Blue Team Mindset, Adversary Simulation<br>
- Fast script, slow coffee, never-ending curiosity<br>
</div>
''', unsafe_allow_html=True)

st.markdown('<div class="terminal-section-title">[PROJECTS]</div>', unsafe_allow_html=True)
st.markdown('''
<div class="term-block">
- SOC-L1 SimLab<br>
- <span class="glitch-effect">[Add more projects here]</span>
</div>
''', unsafe_allow_html=True)

st.markdown('<div class="terminal-section-title">[SOCIAL LINKS]</div>', unsafe_allow_html=True)
st.markdown('''
<div class="term-block">
<a href="https://github.com/kartavyaojha" target="_blank" class="term-link">GitHub</a>
&nbsp;|&nbsp;
<a href="https://www.linkedin.com/in/kartavya-ojha" target="_blank" class="term-link">LinkedIn</a>
&nbsp;|&nbsp;
<a href="mailto:kartavya9977@gmail.com" class="term-link">Email</a>
</div>
''', unsafe_allow_html=True)
