import hashlib
import pandas as pd
from Visualzation import DataVisualization
from Redis import RedisManager


def build_hash_key(data):
    data_str = str(data)
    return hashlib.shake_128(data_str.encode('utf-8')).hexdigest(10)


def load_players_from_csv(file_path):
    df = pd.read_csv(file_path)
    players = []
    teams = set()

    for _, row in df.iterrows():
        player = {
            "name": row["name"],
            "position": row["position"],
            "team": row["team"],
        }
        players.append(player)
        teams.add(row["team"])

    return players, list(teams)


def visualize_data(players):
    visualizer = DataVisualization()
    visualizer.plot_team_distribution(players)


def store_data_in_redis(redis_client, players):
    for player in players:
        player["key"] = build_hash_key(player)
        redis_client.set_info_to_redis(player)


def main():
    # Load data from CSV
    file_path = './data/players_list.csv'
    players, teams = load_players_from_csv(file_path)

    visualize_data(players)
    print(f"There are {len(teams)} teams in the data: {teams}")

    redis_client = RedisManager()
    store_data_in_redis(redis_client, players)

    info = redis_client.get_info_from_redis("Manchester City")
    print(info)

    for team in teams[:]:
        redis_client.remove_info_from_redis(team)

if __name__ == '__main__':
    main()