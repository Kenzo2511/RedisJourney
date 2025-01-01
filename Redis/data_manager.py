import redis
import json

def conver_dict_to_json(data):
    json_data = json.dumps(data)
    return json_data

class RedisManager():
    def __init__(self):
        self.redis_client = redis.Redis( host = "localhost", port = 6379, db = 0 )

    def _set_info_to_redis(self, data):
        cache_key = f"{data['team']}:{data['key']}"
        self.redis_client.set(cache_key, conver_dict_to_json(data))

    def _get_info_from_redis(self, key_word):
        info = []
        pattern = f"{key_word}:*"
        keys = self.redis_client.keys(pattern)

        for key in keys:
            data = self.redis_client.get(key)
            data_detailed = json.loads(data)                
            info.append(f"name: {data_detailed['name']} - position: {data_detailed['position']} ")
        return info
        

    def _remove_info_from_redis(self, key_word):
        pattern = f"{key_word}:*"
        keys = self.redis_client.keys(pattern)

        for key in keys:
            self.redis_client.delete(key)
        print(f"Deleted info by key world: {key_word}")