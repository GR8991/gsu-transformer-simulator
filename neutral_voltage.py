import numpy as np

def neutral_shift(transformer, unbalance_percent=5):
    """
    Computes neutral voltage displacement (per-unit)
    caused by negative-sequence unbalance.
    """
    I2 = unbalance_percent / 100     # convert % to per-unit
    Z0 = transformer.Z[0,0]          # zero-sequence impedance approx

    Vn = (I2 * Z0) / 3               # neutral voltage shift formula
    return Vn
