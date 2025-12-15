import numpy as np
import matplotlib.pyplot as plt

def harmonic_response(tfmr, order, I_mag=0.01):
    I = np.zeros(3)
    I[2] = I_mag
    return order * (tfmr.Z @ I)

def harmonic_barchart(harmonics_dict):
    fig, ax = plt.subplots()
    labels = list(harmonics_dict.keys())
    values = [np.linalg.norm(v) for v in harmonics_dict.values()]
    ax.bar(labels, values, color='steelblue')
    ax.set_title("Harmonic Magnitudes")
    ax.set_ylabel("Magnitude (pu)")
    return fig
