import redis
import json

def convert_dict_to_json(data):
    return json.dumps(data)


class RedisManager:
    def __init__(self, host="localhost", port=6379, db=0):
        self.redis_client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def set_info_to_redis(self, data):
        if "team" not in data or "key" not in data:
            raise ValueError("Data must contain 'team' and 'key' fields.")
        cache_key = f"{data['team']}:{data['key']}"
        self.redis_client.set(cache_key, convert_dict_to_json(data))

    def get_info_from_redis(self, keyword):
        pattern = f"{keyword}:*"
        keys = self.redis_client.keys(pattern)
        info = []

        for key in keys:
            data = self.redis_client.get(key)
            if data:
                player_data = json.loads(data)
                info.append(f"name: {player_data['name']} - position: {player_data['position']} ")
        return info

    def remove_info_from_redis(self, keyword):
        pattern = f"{keyword}:*"
        keys = self.redis_client.keys(pattern)

        for key in keys:
            self.redis_client.delete(key)
        print(f"Deleted all data for keyword: {keyword}")
