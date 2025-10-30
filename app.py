import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Appointment Scheduler", layout="wide")
st.title("💬 Appointment Scheduler")

# Make the Streamlit page background plain white
st.markdown(
    """
    <style>
      .stApp { background: #ffffff; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inject Dialogflow Messenger as a floating popup (bottom-right), like your screenshot
components.html(
    """
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>

    <style>
      /* Float the chat widget like a popup on the page edge */
      df-messenger {
        position: fixed;
        right: 24px;
        bottom: 24px;
        z-index: 999;

        /* Plain, minimal theme */
        --df-messenger-chat-background-color: #ffffff;  /* chat area */
        --df-messenger-font-color: #000000;
        --df-messenger-send-icon: #1a73e8;
        --df-messenger-user-message: #e6f0ff;  /* optional subtle user bubble */
        --df-messenger-bot-message: #f5f5f5;   /* optional subtle bot bubble */
        --df-messenger-button-titlebar-color: #1a73e8; /* header/button color */
      }
    </style>

    <df-messenger
      intent="WELCOME"
      chat-title="AppointmentScheduler"
      agent-id="6672a274-5ba0-477e-8f1d-d3d1dfe9feee"
      language-code="en">
    </df-messenger>
    """,
    height=0,   # widget floats; no space needed in the layout
)
