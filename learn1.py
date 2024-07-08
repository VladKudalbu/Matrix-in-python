import random
import time

script = True

while True:
    num = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)
    num4 = random.randint(1, 9)
    num5 = random.randint(1, 9)
    num6 = random.randint(1, 9)
    num7 = random.randint(1, 9)
    num8 = random.randint(1, 9)
    num9 = random.randint(1, 9)
    time.sleep(0.03)
    print(num, num2, num3, num4, num5, num6, num7, num8, num9)
    if script == False:
        break