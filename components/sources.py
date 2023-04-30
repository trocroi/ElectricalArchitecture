import math
from dataclasses import dataclass

@dataclass
class PerfectVoltageSource:
    Vdc: float = 5  # Voltage, dc offset
    Vac: float = 0  # Voltage, peak to peak
    freq: float = 0  # Hz
    phase: float = 0 # phase offset
    nodeA: any = None
    nodeB: any = None

@dataclass
class PerfectCurrentSource:
    Idc: float = 5  # 1 Amp, dc offset
    Iac: float = 0  # Amps, peak-to-peak
    freq: float = 0  # Hz
    phase: float = 0 # phase offset
    nodeA: any = None
    nodeB: any = None