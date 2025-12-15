import streamlit as st
import numpy as np

def interactive_impedance_editor(ZHL_default, ZHT_default, ZLT_default):
    st.subheader("Impedance Matrix Editor (Interactive)")

    col1, col2, col3 = st.columns(3)

    with col1:
        ZHL = st.number_input("Z(HV–LV) [%]", value=ZHL_default * 100.0) / 100.0

    with col2:
        ZHT = st.number_input("Z(HV–Tertiary) [%]", value=ZHT_default * 100.0) / 100.0

    with col3:
        ZLT = st.number_input("Z(LV–Tertiary) [%]", value=ZLT_default * 100.0) / 100.0

    Z = np.array([
        [ZHL + ZHT, -ZHL, -ZHT],
        [-ZHL, ZHL + ZLT, -ZLT],
        [-ZHT, -ZLT, ZHT + ZLT]
    ])

    st.write("### Updated Impedance Matrix (pu)")
    st.write(Z)

    return ZHL, ZHT, ZLT, Z
