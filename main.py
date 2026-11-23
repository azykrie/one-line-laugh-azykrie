import os
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write("My smart fridge just emailed me a diet plan, so now even my leftovers are judging me.")
