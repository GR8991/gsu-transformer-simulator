import numpy as np

def inrush_waveform(t_max=1.0, steps=500, X_mag=0.2, flux_residual=0.5):
    t = np.linspace(0, t_max, steps)
    voltage = np.sin(2*np.pi*60*t)
    flux = np.cumsum(voltage) * (t[1]-t[0])
    current = (flux + flux_residual) / X_mag
    return t, current
