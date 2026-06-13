import streamlit as st

def footer_home():
    
    st.markdown(f"""
        <div style="margin-top:2rem;display:flex;gap:6px;justify-content:center;align-items:center;">
        <p style="font-weight:bold;color:white">Made with ❤️ by Ansh</p>
        </div>
    """, unsafe_allow_html=True)