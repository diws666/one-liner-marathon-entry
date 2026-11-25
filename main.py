"""One-Liner Marathon entry.

The turn: the fridge doesn't scold you — it one-ups you by involving your
doctor before you've even closed the door. The appliance is the straight man
who becomes the busybody.
"""

JOKE = "My smart fridge caught me sneaking ice cream at 3 a.m. and emailed my doctor before I even closed the door."

with open("/output/entry.txt", "w", encoding="utf-8") as fh:
    fh.write(JOKE)
