import random
import time

while True:
    with open("data.txt", "w") as file:
        file.write(f"{random.randint(0, 9)} {random.randint(0, 9)}")

    time.sleep(1)