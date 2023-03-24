'''from datetime import date

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)'''

from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Fecha y Hora:", dt)
print("Fecha:", dt.date())
print("Hora:", dt.time())
