from passives import Resistor
from sources import PerfectVoltageSource
from nodes import Node

###    A-----[ R1 = 10 Ohm]----B
###    |                       |
###  [ V1 ]                  [ R2 ]
###  [5 Vdc]                 [20 Ohm]
###    |                       |
###    C-----------------------C

V1 = PerfectVoltageSource(5)
R1 = Resistor(10)
R2 = Resistor(20)

A = Node("A")
A.add_connection(V1)
A.add_connection(R1)