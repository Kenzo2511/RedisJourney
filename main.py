from Redis import RedisManager
import hashlib
import pandas as pd
from Visualzation import DataVisualization


def build_hash_key(data):
    data_str = (str(data))
    hash_key = hashlib.shake_128(data_str.encode('utf-8')).hexdigest(10)
    return hash_key

def main():
    players = []
    teams = []
    df = pd.read_csv('./data/players_list.csv')
    visualize = DataVisualization()

    for idx in range(0, len(df)):
        player = {}
        player['name']=df.iloc[idx]['name']
        player['position']=df.iloc[idx]['position']
        player['team']=df.iloc[idx]['team']
        if player['team'] not in teams:
            teams.append(player['team'])
        players.append(player)

    visualize.plot_data(players)
    print(f"There are {len(teams)} in data: ", teams)

    redis_client = RedisManager()
    for player in players:
        player['key']=build_hash_key(player)
        redis_client._set_info_to_redis(player)

    info = redis_client._get_info_from_redis("Manchester City")
    print(info)
    redis_client._remove_info_from_redis(teams[0])
    redis_client._remove_info_from_redis(teams[1])
    redis_client._remove_info_from_redis(teams[2])

if __name__ == '__main__':
    main()