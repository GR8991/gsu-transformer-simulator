import streamlit as st
import numpy as np

from transformer import ThreeWindingTransformer
from sc_analysis import slg_fault_current, three_phase_fault
from neutral_voltage import neutral_shift
from harmonics import harmonic_response, harmonic_barchart
from phasor import plot_phasor
from zero_sequence import zero_sequence_animation
from inrush import inrush_waveform
from sequence_networks import draw_sequence_network
from ui_components import etap_card

st.set_page_config(page_title="GSU Transformer Simulator", layout="wide")

st.title("⚡ GSU Transformer Analysis Suite (115/34.5/13.8 kV)")

ZHL = st.sidebar.slider("HV–LV Impedance", 0.05, 0.20, 0.10)
ZHT = st.sidebar.slider("HV–T Impedance", 0.05, 0.20, 0.12)
ZLT = st.sidebar.slider("LV–T Impedance", 0.05, 0.20, 0.08)

tfmr = ThreeWindingTransformer(ZHL, ZHT, ZLT)

col1, col2, col3 = st.columns(3)

with col1:
    etap_card("SLG Fault Current (pu)", round(slg_fault_current(tfmr), 3))

with col2:
    etap_card("3ϕ Fault Current (pu)", round(three_phase_fault(tfmr), 3))

with col3:
    etap_card("Neutral Shift (pu)", round(neutral_shift(tfmr), 3))

# Harmonic bar chart
harm_dict = {
    "3rd": harmonic_response(tfmr, 3),
    "5th": harmonic_response(tfmr, 5),
    "7th": harmonic_response(tfmr, 7),
}
st.subheader("Harmonic Distortion Magnitudes")
st.pyplot(harmonic_barchart(harm_dict))

# Phasor Diagram
st.subheader("Phasor Diagram (Examples)")
st.pyplot(plot_phasor(0))
st.pyplot(plot_phasor(-120))
st.pyplot(plot_phasor(120))

# Inrush waveform
st.subheader("Inrush Time-Domain Simulation")
t, i = inrush_waveform()
st.line_chart({"Inrush Current": i}, x=t)

# Sequence Network
st.subheader("Sequence Network Diagram")
st.pyplot(draw_sequence_network())
