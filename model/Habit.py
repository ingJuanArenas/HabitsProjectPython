from dataclasses import dataclass, field
from datetime import date

@dataclass
class Habit:
    name: str
    date: date
    completed: bool = field(default=False)

