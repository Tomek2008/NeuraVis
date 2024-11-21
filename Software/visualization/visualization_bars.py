import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

DATA_FILE = "data.txt"

signals = ["Alfa_0", "Alfa_1", "Alfa_2", "Beta_0", "Beta_1", "Beta_2", "Gamma_0", "Gamma_1", "Eta_0", "Eta_1"]

fixed_signals = random.sample(fruits, k=10)

def read_data():
    try:
        with open(DATA_FILE, "r") as file:
            line = file.readline()
            data = list(map(int, line.split()))
            return data
    except FileNotFoundError:
        return []

def update(frame):
    global current_heights
    data = read_data()
    if not data:
        return

    max_value = max(data)
    min_value = min(data)

    if max_value == min_value:
        normalized_data = [400] * len(data)
    else:
        normalized_data = [(datum - min_value) / (max_value - min_value) * (800 - 200) + 200 for datum in data]

    if len(current_heights) != len(normalized_data):
        current_heights = np.zeros(len(normalized_data))

    for i in range(len(normalized_data)):
        current_heights[i] += (normalized_data[i] - current_heights[i]) * 0.2

    ax.clear()

    highest_index = np.argmax(current_heights)

    colors = ['red' if i == highest_index else 'blue' for i in range(len(current_heights))]

    ax.bar(range(len(current_heights)), current_heights, color=colors, width=0.8)
    ax.set_ylim(0, 800)
    ax.set_xlim(-0.5, len(current_heights) - 0.5)
    ax.set_ylabel('Signal Power')
    ax.set_title(f'Data Visualization of EED signal')

    ax.set_xticks(range(len(fixed_signals)))
    ax.set_xticklabels(fixed_signals, rotation=45, ha='right', fontsize=10)

current_heights = []

fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
ani = animation.FuncAnimation(fig, update, interval=50, blit=False, save_count=100)

plt.show()
