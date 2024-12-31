from Redis import RedisManager
import hashlib

players = [
        {"name": "Lionel Messi", "position": "Forward", "team": "Inter Miami CF"},
        {"name": "Cristiano Ronaldo", "position": "Forward", "team": "Al-Nassr"},
        {"name": "Neymar Jr", "position": "Forward", "team": "Al-Hilal"},
        {"name": "Virgil van Dijk", "position": "Defender", "team": "Liverpool"},
    ]

def build_hash_key(data):
    data_str = (str(data))
    hash_key = hashlib.shake_128(data_str.encode('utf-8')).hexdigest(10)
    return hash_key

def main():
    redis_client = RedisManager()
    for player in players:
        player['key']=build_hash_key(player)
        redis_client._set_info_to_redis(player)

    print(redis_client._get_info_from_redis(players[1]))

    redis_client._remove_info_to_redis(players[1])

if __name__ == '__main__':
    main()