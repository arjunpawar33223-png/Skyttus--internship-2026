import random

try:
    x = random.choice([0, 1, "a"])
    print(10 / x)
except Exception as e:
    print("Error:", e)