import random
import time

while True: 
    n = [random.randint(1, 10) for _ in range(9)]
    with open('data.txt', 'w') as file:
        file.write(' '.join(map(str, n)))

    time.sleep(3)
