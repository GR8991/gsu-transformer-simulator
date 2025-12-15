import streamlit as st

def etap_card(title, value):
    st.markdown(f"""
        <div style="padding:15px;border-radius:10px;background:#EEF2F6;">
            <h4>{title}</h4>
            <p style="font-size:22px;color:#2E86C1;"><b>{value}</b></p>
        </div>
    """, unsafe_allow_html=True)
