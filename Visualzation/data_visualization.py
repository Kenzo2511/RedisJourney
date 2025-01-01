# import redis
# import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

class DataVisualization():
    def __init__(self):
        pass

    def plot_position_each_team(self, data):
        grouped_data = defaultdict(list)
        for item in data[1]:
            grouped_data[item["position"]].append(item)
        positions = grouped_data.keys()
        number_of_positions = [len(group_item) for group_item in grouped_data.values()]
        plt.bar(positions, number_of_positions)
        plt.title(f'Number of positions in {data[0]}')
        plt.xlabel('Position')
        plt.ylabel('Number of positions')
        plt.show()

    def plot_data(self, data):
        grouped_data = defaultdict(list)
        for item in data:
            grouped_data[item["team"]].append(item)
        grouped_data = dict(grouped_data)
        teams = grouped_data.keys()
        number_of_playes = [len(group_item) for group_item in grouped_data.values()]
        plt.bar(teams, number_of_playes)
        plt.title('Number of players in teams')
        plt.xlabel('Team')
        plt.ylabel('Number of players')
        plt.show()

        for idx, team in enumerate(teams):
            self.plot_position_each_team(list(grouped_data.items())[idx])
        

        