# One-Line Laugh Sprint entry: a single original funny line (85 chars)
# about everyday life. The program writes it to /output/entry.txt,
# where the gate checks it is 1-200 UTF-8 characters.
import os

LINE = "My smart fridge just emailed me a diet plan, so now even my leftovers are judging me."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
