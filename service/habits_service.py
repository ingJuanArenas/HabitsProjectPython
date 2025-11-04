from dataclasses import dataclass, field
from datetime import datetime
from typing import List


from logger.logger import decorator
from model.Habit import Habit


@dataclass
class HabitsService:
    habits:List[Habit] = field(default_factory= list)

    @decorator
    def add_habit(self, habit: Habit) -> None:
        self.habits.append(habit)
    
    @decorator
    def get_habits(self) -> List[Habit]:
        return self.habits
    
    @decorator
    def get_habits_by_range_of_date(self, date1:datetime, date2:datetime) -> List[Habit]:
        habits_found= [habit for habit in self.habits if date1.date() <= habit.date <= date2.date()]
        return habits_found
    
    @decorator
    def get_habits_by_date(self, date:datetime)-> List[Habit]:
        habits_found = list(filter(lambda h: h.date == date.date(), self.habits))
        return habits_found
    
    @decorator
    def calculate(self):
        habits_completed = list(filter(lambda h: h.completed== True, self.habits))
        percentaje = (len(habits_completed) / len(self.habits))*100
        print(" EL PORCENTAJE DE CUMPLIMIENTO ES: " , percentaje)
    
