import numpy as np
import matplotlib.pyplot as plt

def plot_phasor(angle_deg, magnitude=1.0):
    angle_rad = np.deg2rad(angle_deg)
    x = magnitude * np.cos(angle_rad)
    y = magnitude * np.sin(angle_rad)

    fig, ax = plt.subplots()
    ax.arrow(0, 0, x, y, head_width=0.05, color='red')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True)
    ax.set_title("Phasor Diagram")
    ax.set_aspect("equal")
    return fig
