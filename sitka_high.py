from pathlib import Path
import csv

import matplotlib.pyplot as plt

from datetime import datetime


path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Obtiene fechas y temperaturas màximas de este archivo.
dates, highs = [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# Traza las temperaturas màximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")


# Da formato al trazado.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()    # Dibuja las etiquetas de las fechas diagonalmente
ax.set_ylabel('Temperatura (F)', fontsize=16)
ax.tick_params(labelsize=16)
plt.show()