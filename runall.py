import os

for day in [d for d in os.listdir() if d.startswith("d") and d.endswith(".py")]:
    print(day)
    exec(f"import {day[:-3]}")
