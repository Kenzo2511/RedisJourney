import matplotlib.pyplot as plt
from collections import defaultdict

class DataVisualization:
    def __init__(self):
        pass

    def plot_team_distribution(self, data):
        """
        Plots the number of players in each team.
        :param data: List of dictionaries, each containing player information with "team" key.
        """
        grouped_data = defaultdict(list)
        for item in data:
            grouped_data[item["team"]].append(item)

        teams = list(grouped_data.keys())
        player_counts = [len(players) for players in grouped_data.values()]

        plt.bar(teams, player_counts)
        plt.title('Number of Players in Teams')
        plt.xlabel('Team')
        plt.ylabel('Number of Players')
        plt.show()

        # Plot positions for each team
        for team, players in grouped_data.items():
            self.plot_positions_in_team(team, players)

    def plot_positions_in_team(self, team_name, players):
        """
        Plots the distribution of positions for a given team.
        :param team_name: Name of the team.
        :param players: List of player dictionaries belonging to the team.
        """
        position_counts = defaultdict(int)
        for player in players:
            position_counts[player["position"]] += 1

        positions = list(position_counts.keys())
        counts = list(position_counts.values())

        plt.bar(positions, counts)
        plt.title(f'Position Distribution in Team: {team_name}')
        plt.xlabel('Position')
        plt.ylabel('Number of Players')
        plt.show()
