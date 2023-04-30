import math
from dataclasses import dataclass

@dataclass
class Node:
    name: str = 'default'
    V: float = 0
    I: float = 0
    connect: list = []

    def add_connection(self, item):
        self.connect.append(item)