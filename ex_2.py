import numpy as np

# character_levels = np.array([80, 70, 65, 60])
# print("1D Array (Character Levels):", character_levels)
# print("Shape of 1D array:", character_levels.shape)
#
# team_stats = np.array([
#     [4235.5, 1256.75],  # Kafka
#     [3870.2, 1100.45],  # Black Swan
#     [2985.7, 850.30],   # Tingyun
#     [4500.1, 600.15]    # Huohuo
# ])
# print("\n2D Array (Team Stats):")
# print(team_stats)
# print("Shape of 2D array:", team_stats.shape)

##################################################################################################

# character_levels = np.array([80, 70, 65, 60])
# energy_costs = np.array([10, 12, 15, 20])
#
# level_plus_energy = character_levels + energy_costs
# print("Character Levels + Energy Costs:", level_plus_energy)
#
# level_times_energy = character_levels * energy_costs
# print("Character Levels * Energy Costs:", level_times_energy)
#
# team_1_stats = np.array([
#     [4235.5, 1256.75],  # Kafka
#     [3870.2, 1100.45]   # Black Swan
# ])
# team_2_stats = np.array([
#     [2985.7, 850.30],   # Tingyun
#     [4500.1, 600.15]    # Huohuo
# ])
#
# team_stats_sum = team_1_stats + team_2_stats
# print("\nTeam Stats Sum (HP and ATK):")
# print(team_stats_sum)
#
# team_stats_product = team_1_stats * team_2_stats
# print("\nTeam Stats Product (HP and ATK):")
# print(team_stats_product)

##################################################################################################

# energy_recharge = np.arange(0, 1.1, 0.1)
# print("Energy Recharge Progress (0 to 1 with step 0.1):", energy_recharge)

##################################################################################################

attack_stats = np.array([1256.75, 1100.45, 850.30, 600.15])  # Kafka, Black Swan, Tingyun, Huohuo
damage_multipliers = np.array([1.5, 1.2, 1.0, 0.8])

dot_product = np.dot(attack_stats, damage_multipliers)
print("Scalar Dot Product of Attack Stats and Damage Multipliers:", dot_product)