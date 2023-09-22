from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, ("es_MX", "UTF-8"))

def get_hours():
    current_datetime = datetime.now()
    # Formato de hora: HH:MM:SS
    formatted_time = current_datetime.strftime("%I:%M:%S %p")
    return formatted_time

def get_date():
    current_datetime = datetime.now()
    # Formato de fecha: día_semana, día de mes de año
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_semana = dias_semana[current_datetime.weekday()]
    formatted_date = current_datetime.strftime(f"{dia_semana}, %d de %B de %Y")
    return formatted_date



