from typing import List
from model.Habit import Habit
from datetime import datetime

from service.habits_service import HabitsService

service= HabitsService()

def get_habit_info_toadd()->Habit:
    print("Registrar nuevo hábito del día")
    name = input("Nombre del hábito: ")
    date = datetime.strptime(input("Fecha del hábito (YYYY-MM-DD): "), "%Y-%m-%d").date()
    completed= input("¿Ha completado el hábito? (S/N): ").lower() == "s"
    habit = Habit(name, date, completed)
    return habit

def print_data_found(data:List[Habit])-> None:
    if len(data) == 0:
        print("No hay datos...")
    else:
        for habit in data:
            print(habit)

try:
    while True:
        print(""" 
    ===========================================
            ANALIZADOR DE HÁBITOS DIARIOS
    ===========================================
    Seleccione una opción:

    Registrar nuevo hábito del día
    Listar hábitos de un día específico
    Listar hábitos por rango de fechas
    Calcular porcentaje de cumplimiento
    """)
        option = int(input("Opción: "))
        match option:
            case 1:
                habit = get_habit_info_toadd()
                service.add_habit(habit=habit)
            case 2:
                print("Listar hábitos de un día específico")
                date = datetime.strptime(input("Fecha del día (YYYY-MM-DD): "), "%Y-%m-%d")
                print_data_found(service.get_habits_by_date(date))
            case 3:
                print("Listar hábitos por rango de fechas")
                date1 = datetime.strptime(input("Fecha inicial (YYYY-MM-DD): "), "%Y-%m-%d")
                date2 = datetime.strptime(input("Fecha final (YYYY-MM-DD): "), "%Y-%m-%d")
                print_data_found(service.get_habits_by_range_of_date(date1, date2))
            case 4:
                print("Calcular porcentaje de cumplimiento")
                service.calculate()
            case 0: break
            case _: 
                print("Opcion invalida")
except ValueError as e:
    print("ERROR: " ,e )
except Exception as e:
    print("ERROR: " , e)

