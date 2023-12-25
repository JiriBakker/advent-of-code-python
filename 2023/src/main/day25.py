from __future__ import annotations
from dataclasses import dataclass

def day25a(input: list[str]) -> int:
    return 0

@dataclass
class Component(object):
    name: str
    neighbours: list[Component]

