import numpy as np
import matplotlib.pyplot as plt

def zero_sequence_animation(frames=20):
    figs = []
    for i in range(frames):
        fig, ax = plt.subplots()
        angle = 2*np.pi * (i/frames)
        x = np.cos(angle)
        y = np.sin(angle)
        ax.plot([0,x], [0,y], color='orange')
        ax.set_xlim(-1.2,1.2)
        ax.set_ylim(-1.2,1.2)
        ax.set_title("Zero Sequence Circulating Current")
        figs.append(fig)
    return figs
