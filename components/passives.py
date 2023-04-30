from dataclasses import dataclass

@dataclass
class Resistor():
    R: float
    power: float = -1  # any positive value indicates resistor power
    nodeA: any = None
    nodeB: any = None

    def nodeB_voltage(self):
        return nodeA.V - (nodeA.I * self.R)
    
    def nodeB_current(self):
        return nodeA.I

@dataclass
class Capacitor:
    C: float = 1  # farad...
    Vmax: float = -1  # -1 indicates no limit
    nodeA: any = None
    nodeB: any = None