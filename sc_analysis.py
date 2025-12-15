def slg_fault_current(tfmr, V_pu=1.0):
    Z1 = tfmr.Z[1,1]
    Z2 = tfmr.Z[1,1]
    Z0 = tfmr.Z[1,1]
    return V_pu / (Z1 + Z2 + Z0)

def three_phase_fault(tfmr, V_pu=1.0):
    return V_pu / tfmr.Z[1,1]
