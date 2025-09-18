import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = x^2 (Attack Power Scaling)', color='purple')
plt.xlabel('Level Difference (Character Level)')
plt.ylabel('Attack Power')
plt.title('Honkai Star Rail: Attack Power Scaling Model')
plt.grid(True)

# another curve (y = x^3) with different color and legend
y_cubic = x**3
plt.plot(x, y_cubic, label='y = x^3 (Energy Recharge Scaling)', color='cyan', linestyle='--')
plt.legend()

plt.show()

# histogram of random data (simulating character damage)
np.random.seed(42)  # For reproducibility
character_damage = np.random.normal(loc=1000, scale=200, size=1000)  # Simulating damage values
plt.figure(figsize=(8, 6))
plt.hist(character_damage, bins=30, color='magenta', alpha=0.7)
plt.xlabel('Damage Dealt by Characters')
plt.ylabel('Frequency')
plt.title('Histogram of Simulated Damage in Honkai Star Rail')
plt.grid(True)
plt.show()