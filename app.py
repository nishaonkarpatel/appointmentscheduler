import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Appointment Scheduler", layout="wide")
st.title("💬 Appointment Scheduler")

# Keep page background plain
st.markdown(
    "<style>.stApp{background:#ffffff;}</style>",
    unsafe_allow_html=True,
)

# Render Dialogflow Messenger inside a visible iframe
components.html(
    """
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>

    <style>
      /* Position inside the iframe (bottom-right look) */
      df-messenger {
        position: fixed;
        right: 16px;
        bottom: 16px;
        z-index: 999;

        /* simple, plain theme */
        --df-messenger-chat-background-color: #ffffff;
        --df-messenger-font-color: #000000;
        --df-messenger-button-titlebar-color: #1a73e8;
        --df-messenger-user-message: #e6f0ff;
        --df-messenger-bot-message: #f5f5f5;
      }
      /* Remove default page spacing inside the iframe */
      body { margin: 0; }
    </style>

    <df-messenger
      intent="WELCOME"
      chat-title="AppointmentScheduler"
      agent-id="6672a274-5ba0-477e-8f1d-d3d1dfe9feee"
      language-code="en">
    </df-messenger>
    """,
    height=640,   # <-- give it room to display
    width=420,    # optional; adjust to taste
    scrolling=False
)
