import numpy as np

class ThreeWindingTransformer:
    def __init__(self, ZHL=0.10, ZHT=0.12, ZLT=0.08):
        self.ZHL = ZHL
        self.ZHT = ZHT
        self.ZLT = ZLT
        self.Z = self.build_impedance_matrix()

    def build_impedance_matrix(self):
        ZHH = self.ZHL + self.ZHT
        ZLL = self.ZHL + self.ZLT
        ZTT = self.ZHT + self.ZLT

        Z = np.array([
            [ZHH, -self.ZHL, -self.ZHT],
            [-self.ZHL, ZLL, -self.ZLT],
            [-self.ZHT, -self.ZLT, ZTT]
        ])
        return Z
