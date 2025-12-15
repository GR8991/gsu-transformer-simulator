import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import local modules
from transformer import ThreeWindingTransformer
from sc_analysis import slg_fault_current, three_phase_fault
from neutral_voltage import neutral_shift
from harmonics import harmonic_response, harmonic_barchart
from phasor import plot_phasor
from zero_sequence import zero_sequence_animation
from inrush import inrush_waveform
from sequence_networks import draw_sequence_network
from ui_components import etap_card
from impedance_editor import interactive_impedance_editor
from iec_ieee_compliance import check_short_circuit_withstand, check_insulation_levels


# -----------------------------------------------------------------------------
# STREAMLIT PAGE SETTINGS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="GSU Transformer Simulator",
    layout="wide",
)

st.title("⚡ GSU Transformer Analysis Suite (115 / 34.5 / 13.8 kV)")

st.markdown("""
This tool simulates a **three-winding GSU transformer** using:
- Impedance matrix modeling  
- Fault current analysis  
- Harmonic distortion  
- Neutral voltage displacement  
- Energization inrush  
- Sequence network diagrams  
- Phasor visualization  

Designed for education, research, and power system design.
""")

# -----------------------------------------------------------------------------
# USER INPUTS
# -----------------------------------------------------------------------------
st.sidebar.header("Transformer Parameters")

ZHL = st.sidebar.slider("HV–LV Impedance (pu)", 0.05, 0.30, 0.10)
ZHT = st.sidebar.slider("HV–Tertiary Impedance (pu)", 0.05, 0.30, 0.12)
ZLT = st.sidebar.slider("LV–Tertiary Impedance (pu)", 0.05, 0.30, 0.08)

#tfmr = ThreeWindingTransformer(ZHL, ZHT, ZLT)
# -----------------------------------------------------------------------------
# INTERACTIVE IMPEDANCE EDITOR  (INSERTED HERE - PART 4)
# -----------------------------------------------------------------------------
st.subheader("🧮 Interactive Impedance Editor")

ZHL, ZHT, ZLT, edited_Z = interactive_impedance_editor(ZHL, ZHT, ZLT)

tfmr = ThreeWindingTransformer(ZHL, ZHT, ZLT)

st.success("Impedance matrix updated successfully!")


# -----------------------------------------------------------------------------
# SECTION 1: FAULT CURRENTS
# -----------------------------------------------------------------------------
st.subheader("📌 Fault Current Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    etap_card("SLG Fault Current (pu)", round(slg_fault_current(tfmr), 4))

with col2:
    etap_card("3-Phase Fault Current (pu)", round(three_phase_fault(tfmr), 4))

with col3:
    etap_card("Neutral Shift (pu)", round(neutral_shift(tfmr), 4))

# -----------------------------------------------------------------------------
# SECTION 2: IMPEDANCE MATRIX
# -----------------------------------------------------------------------------
st.subheader("📘 Transformer Impedance Matrix (per-unit)")
st.write(tfmr.Z)

# -----------------------------------------------------------------------------
# SECTION 3: HARMONIC ANALYSIS
# -----------------------------------------------------------------------------
st.subheader("🎵 Harmonic Analysis (3rd, 5th, 7th Harmonics)")

harm_dict = {
    "3rd": harmonic_response(tfmr, 3),
    "5th": harmonic_response(tfmr, 5),
    "7th": harmonic_response(tfmr, 7),
}

fig_harm = harmonic_barchart(harm_dict)
st.pyplot(fig_harm)

# -----------------------------------------------------------------------------
# SECTION 4: PHASOR DIAGRAMS
# -----------------------------------------------------------------------------
st.subheader("📐 Phasor Diagram Visualization")

ph_col1, ph_col2, ph_col3 = st.columns(3)

with ph_col1:
    st.pyplot(plot_phasor(0))

with ph_col2:
    st.pyplot(plot_phasor(-120))

with ph_col3:
    st.pyplot(plot_phasor(120))

# -----------------------------------------------------------------------------
# SECTION 5: INRUSH CURRENT SIMULATION
# -----------------------------------------------------------------------------
st.subheader("⚡ Inrush Current (Time-Domain Simulation)")

t, i = inrush_waveform()

df_inrush = pd.DataFrame({"Time (s)": t, "Inrush Current (pu)": i})
st.line_chart(df_inrush, x="Time (s)", y="Inrush Current (pu)")

# -----------------------------------------------------------------------------
# SECTION 6: SEQUENCE NETWORKS
# -----------------------------------------------------------------------------
st.subheader("🔗 Sequence Network Diagram")
seq_fig = draw_sequence_network()
st.pyplot(seq_fig)

# -----------------------------------------------------------------------------
# SECTION 7: ZERO-SEQUENCE CURRENT ANIMATION (STATIC FRAME)
# -----------------------------------------------------------------------------
st.subheader("🌀 Zero-Sequence Circulating Current (Example Frame)")

# Take 1 frame of animation
zero_frames = zero_sequence_animation(frames=1)
st.pyplot(zero_frames[0])



st.subheader("📘 IEC / IEEE Compliance Checks")

colA, colB = st.columns(2)

with colA:
    st.markdown("### IEC 60076-5 Short-Circuit Withstand Check")
    compliance = check_short_circuit_withstand(125, ZHL * 100)
    st.write(compliance)

with colB:
    st.markdown("### IEC 60076-3 Insulation Level Recommendation")
    hv_bil = check_insulation_levels(115)
    st.write(hv_bil)

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
Built for power system engineers, researchers, and students.  
**Transformer Analysis Suite – Python + Streamlit**
""")
