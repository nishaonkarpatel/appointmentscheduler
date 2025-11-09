import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Dialogflow Bot", page_icon="🤖")

components.html(
    """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <!-- Dialogflow Messenger script -->
        <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
      </head>
      <body>
        <!-- The actual chat widget -->
        <df-messenger
          intent="WELCOME"
          chat-title="AppointmentScheduler"
          agent-id="06a31fc3-12d5-4de7-9e62-878943f9f1bf"
          language-code="en">
        </df-messenger>
      </body>
    </html>
    """,
    height=600,   # adjust so the chat fits
    width=400,    # or just remove width to auto-fit
)
