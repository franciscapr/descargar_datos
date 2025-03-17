from pathlib import Path
import csv

import matplotlib.pyplot as plt


path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extraer las temperaturas màximas.

highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)

# Traza las temperatuas màximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Da formato al trazado.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatura (F)', fontsize=16)
ax.tick_params(labelsize=16)
plt.show()