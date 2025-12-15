import numpy as np
import pandas as pd

def check_short_circuit_withstand(S_MVA, Z_percent, X_over_R=10):
    """
    IEEE C57 / IEC 60076-5 short-circuit current & mechanical withstand check.
    S_MVA  = transformer MVA rating
    Z_percent = % impedance (HV–LV)
    X_over_R = typical 10 for GSU
    """
    Z_pu = Z_percent / 100
    I_rated = S_MVA / (np.sqrt(3))  # base current in pu system
    I_sc = 1 / Z_pu                  # pu short-circuit current
    
    I_asym = I_sc * np.sqrt(1 + (X_over_R)**2) / X_over_R
    
    return {
        "I_rated_pu": round(I_rated, 3),
        "I_sym_sc_pu": round(I_sc, 3),
        "I_asym_sc_pu": round(I_asym, 3),
        "Pass?": "YES" if I_asym < 25 else "NO"
    }


def check_insulation_levels(voltage_kV):
    """
    IEC 60076-3 BIL level recommendations
    """
    table = {
        11: 95,
        13.8: 110,
        34.5: 150,
        66: 250,
        115: 325,
        132: 350
    }
    
    if voltage_kV in table:
        return {
            "Voltage kV": voltage_kV,
            "Recommended BIL (kVp)": table[voltage_kV],
            "Standard": "IEC 60076-3"
        }
    else:
        return {"Error": "Voltage level not in IEC table."}
